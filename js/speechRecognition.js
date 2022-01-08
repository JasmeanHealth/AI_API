const iconv = require("iconv-lite");
var exec = require("child_process").execSync;
let rs;
const Test = () => {
  rs = exec(`python ../python/speechRecognition.py`);
  rs = iconv.decode(rs, "euc-kr");
};

Test();
console.log(rs);
