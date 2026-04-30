



const userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
let o = {
    method: r,
    timeStamp: i || +new Date(),
    'User-Agent': window.btoa("".concat(userAgent)),
    index: Math.floor(1e3 * Math.random() + 1),
    channelId: 40009,
    sVersion: 2,
    key: 'A013F70DB97834C0A5492378BD76C53A'
};

var d = Object.keys(o).reduce(function (t, e) {
    return o[e] === 0 || o[e] ? "".concat(t, "&").concat(e, "=").concat(o[e]) : "".concat(t, "&").concat(e, "=''");
  }, '').slice(1);
var s;

try {
    s = md5_default()(d.replace(/\s+/g, ' '));
} catch (t) {
    console.log('error', t), s = '';
}