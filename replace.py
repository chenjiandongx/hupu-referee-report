import re

origin = """"""

step1 = re.sub("(\d+\.)", "\g<1> ", origin)
step2 = re.sub("(\d+)、", "\g<1>. ", step1)
step3 = re.sub("-", "", step2)
step4 = re.sub("(\d+\. \S+)", "**\g<1>**", step3)

step5 = """
<details>
<summary>【虎扑步行街20个简短而深刻的亮回复】第 期！</summary>\n""" + step4 + "\n</details>"

print(step5)
