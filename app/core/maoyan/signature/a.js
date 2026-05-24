const CryptoJS = require('crypto-js');

// ============ 配置区 ============
const userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0";

// 时间戳:如果有外部传入的 browerTime 就用它,否则用当前时间
const browerTime = null;  // 这里填你的 browerTime,没有就保持 null
const i = browerTime ? new Date(browerTime).valueOf() : null;

// ============ 签名生成 ============
const o = {
    method: "GET",
    timeStamp: i || +new Date(),
    'User-Agent': Buffer.from(userAgent).toString('base64'),  // Node.js 替代 window.btoa
    index: Math.floor(1e3 * Math.random() + 1),
    channelId: 40009,
    sVersion: 2,
    key: 'A013F70DB97834C0A5492378BD76C53A'
};

// 拼接成 key=value&key=value 的字符串
const d = Object.keys(o).reduce(function (t, e) {
    return o[e] === 0 || o[e]
        ? "".concat(t, "&").concat(e, "=").concat(o[e])
        : "".concat(t, "&").concat(e, "=''");
}, '').slice(1);

// MD5 签名
let s;
try {
    s = CryptoJS.MD5(d.replace(/\s+/g, ' ')).toString();
} catch (t) {
    console.log('error', t);
    s = '';
}


console.log('MD5 签名:', s);
console.log(o);
