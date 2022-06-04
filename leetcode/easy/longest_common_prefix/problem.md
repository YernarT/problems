# 最长公共前缀

> 来源: 力扣（LeetCode）<br /> 链接: https://leetcode.com/problems/longest-common-prefix/

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""

 
## 示例 1: 

```python
# 输入: 
strs = ["flower", "flow", "flight"]
# 输出: 
"fl"
```

## 示例 2: 

```python
# 输入: 
strs = ["dog", "racecar", "car"]
# 输出: 
""
# 解释: 输入不存在公共前缀。
```
 

## 提示: 

`1 <= strs.length <= 200`

`0 <= strs[i].length <= 200`

`strs[i]` 仅由小写英文字母组成