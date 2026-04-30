const crypto = require('crypto');

function zN(input) {  
  if (typeof input !== 'string') input = input.toString();
  return crypto.createHash('md5').update(input).digest('hex');
}

const t = {
  stringToBytes: function(str) {
    return new Uint8Array(Buffer.from(str, 'utf-8'));
  }
};

const r = {
  stringToBytes: function(str) {
    const bytes = new Uint8Array(str.length);
    for (let i = 0; i < str.length; i++) {
      bytes[i] = str.charCodeAt(i) & 0xff;
    }
    return bytes;
  }
};

function n(obj) {
  return obj instanceof ArrayBuffer ||
         obj instanceof Uint8Array ||
         obj instanceof Uint8ClampedArray ||
         obj instanceof Int8Array ||
         obj instanceof Uint16Array ||
         obj instanceof Int16Array ||
         obj instanceof Uint32Array ||
         obj instanceof Int32Array ||
         obj instanceof Float32Array ||
         obj instanceof Float64Array;
}

const e = {
  bytesToWords: function(bytes) {
    const words = [];
    for (let i = 0, b = 0; i < bytes.length; i++, b += 8) {
      words[b >>> 5] |= bytes[i] << (24 - b % 32);
    }
    return words;
  },
  wordsToBytes: function(words) {
    const bytes = [];
    for (let i = 0; i < words.length * 32; i += 8) {
      bytes.push((words[i >>> 5] >>> (24 - i % 32)) & 0xff);
    }
    return bytes;
  },
  bytesToHex: function(bytes) {
    return Buffer.from(bytes).toString('hex');
  },
  endian: function(words) {
    return words; // little-endian，直接返回
  }
};


function ff(i, s, a, c, l, u, d) {
  var f = i + (s & a | ~s & c) + (l >>> 0) + d;
  return (f << u | f >>> 32 - u) + s;
}

function gg(i, s, a, c, l, u, d) {
  var f = i + (s & c | a & ~c) + (l >>> 0) + d;
  return (f << u | f >>> 32 - u) + s;
}

function hh(i, s, a, c, l, u, d) {
  var f = i + (s ^ a ^ c) + (l >>> 0) + d;
  return (f << u | f >>> 32 - u) + s;
}

function ii(i, s, a, c, l, u, d) {
  var f = i + (a ^ (s | ~c)) + (l >>> 0) + d;
  return (f << u | f >>> 32 - u) + s;
}


function KN(key) {
  const positions = [46,47,18,2,53,8,23,32,15,50,10,31,58,3,45,35,27,43,5,49,33,9,42,19,29,28,14,39,12,38,41,13,37,48,7,16,24,55,40,61,26,17,0,1,60,51,30,4,22,25,54,21,56,59,6,63,57,62,11,36,20,34,44,52];
  let result = '';
  positions.forEach(pos => {
    if (pos < key.length) {
      result += key.charAt(pos);
    }
  });
  return result.slice(0, 32);
}

function YN(config) {
  if (config.useAssignKey) {
    return {
      imgKey: config.wbiImgKey,
      subKey: config.wbiSubKey
    };
  }

  const stored = null; // GN("wbi_img_urls") 返回 null
  const parts = stored ? stored.split("-") : [];
  return {
    imgKey: parts[0] || config.wbiImgKey,
    subKey: parts[1] || config.wbiSubKey
  };
}

function XN(params, config = { wbiImgKey: "", wbiSubKey: "" }) {
  const { imgKey, subKey } = YN(config);
  if (!imgKey || !subKey) return null;

  const mixinKey = KN(imgKey + subKey);
  const wts = Math.round(Date.now() / 1000);

  const fullParams = { ...params, wts };
  const sortedKeys = Object.keys(fullParams).sort();
  const parts = [];

  for (let key of sortedKeys) {
    let value = fullParams[key];
    if (value != null) {
      if (typeof value === "string") {
        value = value.replace(/[!'()*]/g, "");
      }
      parts.push(`${encodeURIComponent(key)}=${encodeURIComponent(value)}`);
    }
  }

  const query = parts.join("&");
  const toSign = query + mixinKey;
  const w_rid = zN(toSign);

  return {
    w_rid,
    wts: wts.toString()
  };
}

// === 测试数据（你提供的） ===
// const params = {
//   pn: 4,
//   ps: 40,
//   tid: 0,
//   special_type: "",
//   order: "pubdate",
//   mid: 1166997747,
//   index: 0,
//   keyword: "",
//   order_avoided: "true",
//   platform: "web",
//   web_location: "333.1387",
//   dm_img_list: "[{\"x\":1290,\"y\":1122,\"z\":0,\"timestamp\":246860,\"k\":121,\"type\":0},{\"x\":1363,\"y\":1182,\"z\":66,\"timestamp\":246960,\"k\":112,\"type\":0},{\"x\":1561,\"y\":766,\"z\":59,\"timestamp\":247060,\"k\":91,\"type\":0},{\"x\":2301,\"y\":-1991,\"z\":181,\"timestamp\":247161,\"k\":93,\"type\":0},{\"x\":2557,\"y\":-2546,\"z\":363,\"timestamp\":247262,\"k\":94,\"type\":0},{\"x\":2262,\"y\":-3011,\"z\":95,\"timestamp\":247363,\"k\":73,\"type\":0},{\"x\":2985,\"y\":-3470,\"z\":431,\"timestamp\":247462,\"k\":101,\"type\":0},{\"x\":3051,\"y\":-3660,\"z\":345,\"timestamp\":247563,\"k\":71,\"type\":0},{\"x\":3760,\"y\":-2939,\"z\":650,\"timestamp\":247663,\"k\":114,\"type\":0},{\"x\":3426,\"y\":-3324,\"z\":308,\"timestamp\":247763,\"k\":74,\"type\":0},{\"x\":3331,\"y\":-3461,\"z\":224,\"timestamp\":247863,\"k\":108,\"type\":0},{\"x\":3861,\"y\":-2934,\"z\":763,\"timestamp\":247963,\"k\":88,\"type\":0},{\"x\":3629,\"y\":-3166,\"z\":531,\"timestamp\":2471104,\"k\":116,\"type\":1},{\"x\":2033,\"y\":2237,\"z\":869,\"timestamp\":2471408,\"k\":76,\"type\":0},{\"x\":2312,\"y\":2159,\"z\":1046,\"timestamp\":2471508,\"k\":109,\"type\":0},{\"x\":2526,\"y\":1668,\"z\":1006,\"timestamp\":2471608,\"k\":76,\"type\":0},{\"x\":3197,\"y\":1558,\"z\":1421,\"timestamp\":2471709,\"k\":68,\"type\":0},{\"x\":3364,\"y\":1004,\"z\":1428,\"timestamp\":2471809,\"k\":89,\"type\":0},{\"x\":2917,\"y\":507,\"z\":970,\"timestamp\":2471909,\"k\":108,\"type\":0},{\"x\":2934,\"y\":527,\"z\":978,\"timestamp\":2472013,\"k\":76,\"type\":0},{\"x\":2384,\"y\":-232,\"z\":388,\"timestamp\":2472114,\"k\":73,\"type\":0},{\"x\":4191,\"y\":1568,\"z\":2193,\"timestamp\":2472217,\"k\":65,\"type\":0},{\"x\":2295,\"y\":-615,\"z\":215,\"timestamp\":2472318,\"k\":84,\"type\":0},{\"x\":4284,\"y\":764,\"z\":1941,\"timestamp\":2472418,\"k\":85,\"type\":0},{\"x\":3990,\"y\":-1773,\"z\":1108,\"timestamp\":2472518,\"k\":111,\"type\":0},{\"x\":5301,\"y\":-1310,\"z\":2180,\"timestamp\":2472619,\"k\":103,\"type\":0},{\"x\":3442,\"y\":-3440,\"z\":260,\"timestamp\":2472735,\"k\":82,\"type\":0},{\"x\":5704,\"y\":-1171,\"z\":2524,\"timestamp\":2472871,\"k\":79,\"type\":0},{\"x\":3507,\"y\":-3312,\"z\":343,\"timestamp\":2472971,\"k\":90,\"type\":0},{\"x\":3319,\"y\":-3500,\"z\":155,\"timestamp\":2495248,\"k\":88,\"type\":1},{\"x\":3088,\"y\":3323,\"z\":1900,\"timestamp\":2495351,\"k\":99,\"type\":0},{\"x\":2418,\"y\":2399,\"z\":1164,\"timestamp\":2495451,\"k\":74,\"type\":0},{\"x\":1788,\"y\":454,\"z\":40,\"timestamp\":2495551,\"k\":112,\"type\":0},{\"x\":4998,\"y\":2689,\"z\":3001,\"timestamp\":2495652,\"k\":84,\"type\":0},{\"x\":2374,\"y\":-135,\"z\":310,\"timestamp\":2495753,\"k\":112,\"type\":0},{\"x\":4270,\"y\":1054,\"z\":1958,\"timestamp\":2495854,\"k\":98,\"type\":0},{\"x\":4279,\"y\":-982,\"z\":1478,\"timestamp\":2495956,\"k\":105,\"type\":0},{\"x\":5785,\"y\":-457,\"z\":2569,\"timestamp\":2496057,\"k\":121,\"type\":0},{\"x\":4613,\"y\":-1841,\"z\":1343,\"timestamp\":2496157,\"k\":103,\"type\":0},{\"x\":6375,\"y\":-398,\"z\":3073,\"timestamp\":2496257,\"k\":94,\"type\":0},{\"x\":4942,\"y\":-1912,\"z\":1607,\"timestamp\":2496357,\"k\":71,\"type\":0},{\"x\":5212,\"y\":-1596,\"z\":1854,\"timestamp\":2496458,\"k\":97,\"type\":0},{\"x\":7249,\"y\":531,\"z\":3874,\"timestamp\":2496559,\"k\":97,\"type\":0},{\"x\":5956,\"y\":-725,\"z\":2562,\"timestamp\":2496659,\"k\":126,\"type\":0},{\"x\":7047,\"y\":375,\"z\":3649,\"timestamp\":2496759,\"k\":90,\"type\":0},{\"x\":8036,\"y\":1364,\"z\":4638,\"timestamp\":2496867,\"k\":126,\"type\":1},{\"x\":5072,\"y\":-1598,\"z\":1668,\"timestamp\":2496973,\"k\":85,\"type\":0},{\"x\":8721,\"y\":2053,\"z\":5311,\"timestamp\":2497081,\"k\":122,\"type\":0},{\"x\":3511,\"y\":-3160,\"z\":87,\"timestamp\":2497182,\"k\":112,\"type\":0},{\"x\":3851,\"y\":-2818,\"z\":421,\"timestamp\":2497283,\"k\":71,\"type\":0}]",
//   dm_img_str: "V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ",
//   dm_cover_img_str: "QU5HTEUgKE5WSURJQSwgTlZJRElBIEdlRm9yY2UgUlRYIDQwNzAgTGFwdG9wIEdQVSAoMHgwMDAwMjg2MCkgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSlHb29nbGUgSW5jLiAoTlZJRElBKQ",
//   dm_img_inter: "{\"ds\":[{\"t\":7,\"c\":\"dnVpX2J1dHRvbiB2dWlfYnV0dG9uLS1hY3RpdmUgdnVpX2J1dHRvbi0tYWN0aXZlLWJsdWUgdnVpX2J1dHRvbi0tbm8tdHJhbnNpdGlvbiB2dWlfcGFnZW5hdGlvbi0tYnRuIHZ1aV9wYWdlbmF0aW9uLS1idG4tbn\",\"p\":[5898,28,9356],\"s\":[449,619,898]}],\"wh\":[3552,1514,4],\"of\":[4703,6522,377]}"
// };

params = {
    "oid": "116243205980425",
    "type": 1,
    "mode": 3,
    "pagination_str": '{"offset":""}',
    "plat": 1,
    "seek_rpid": "",
    "web_location": 1315875,
}

const config = {
  wbiImgKey: "c458435a75b1419ca98ab6d88b4c60d4",
  wbiSubKey: "446140f6859f439e9dd83f7ef858d1cd"
};

const result = XN(params, config);
console.log("签名结果：", result);
console.log("签名长度：", result['w_rid'].length);
console.log("abb5b7e2ed782adf08be04a6718f2ae0".length)