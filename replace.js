var origin = ``

var res = origin
    .replace(/(\d+\.)/g, "$1")
    .replace(/(\d+)、/g, "$1. ")
    .replace(/-/g, "")
    .replace(/(\d+\. \S+)/g, "**$1**")
    .replace(/  /g, " ")

res = `
<details>
<summary>【虎扑步行街20个简短而深刻的亮回复】第 X 期！</summary>\n` + res + "\n\n</details>"

console.log(res)
