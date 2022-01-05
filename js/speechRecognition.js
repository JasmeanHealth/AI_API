const iconv = require("iconv-lite");

var exec = require("child_process").execSync;

let rs = exec(
  `python F:/JasmeanHealth/AI_API/speechRecognition/speechRecognition.py`
);
rs = iconv.decode(rs, "euc-kr");

console.log(rs);
