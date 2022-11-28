# paddlenlp-flask
paddlenlp with flask

## Usage

```
sudo docker-compose up

curl http://localhost:5000/uie -H 'Content-Type: application/json' -d '{
    "schema":["姓名", "毕业院校", "职位", "月收入", "身体状况"],
    "text": "兹证明凌霄为本单位职工，已连续在我单位工作5 年。学历为嘉利顿大学毕业，目前在我单位担任总经理助 理  职位。近一年内该员工在我单位平均月收入（税后）为  12000 元。该职工身体状况良好。本单位仅此承诺上述表述是正确的，真实的。"
}'
```
