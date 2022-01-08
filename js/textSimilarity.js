const iconv = require("iconv-lite");
var exec = require("child_process").execSync;
let rs = exec(`python ../python/textSimilarity.py`);
rs = iconv.decode(rs, "euc-kr");
let data = JSON.parse(rs);
data = { result: data };
console.log(data);
