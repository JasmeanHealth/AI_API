const iconv = require("iconv-lite");
var exec = require("child_process").execSync;

let rs = exec(`python ../python/speechRecognition.py`);
rs = iconv.decode(rs, "euc-kr");

console.log(rs);
