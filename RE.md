# Thư viện Regular Expression trong Python

## Khái niệm biểu thức chính quy 
Biểu thức chính quy là các mẫu dùng để tìm kiếm các bộ kí tự được kết hợp với nhau trong các chuỗi kí tự. Các nhóm kí tự, kí hiệu được viết ra theo quy luật tạo thành mẫu và nó được sử dụng để tìm kiếm văn bản.

Một biểu thức chính quy là một mẫu (pattern) nó tương đồng quy luật với một chuỗi từ trái qua phải. 
Trong Python3 có thư viện `re` hỗ trợ làm việc với biểu thức chính quy. Doc đầy đủ về thư viện này có thể tham khảo tại [đây](https://docs.python.org/2/library/re.html#module-re). 

![image](https://github.com/user-attachments/assets/3d9b08fc-ddba-4055-a33e-ec460f244551)

Ta sẽ tìm hiểu qua một số biểu thức chính quy cơ bản 

# Một số biểu thức chính quy
## Basic Matchers
Xét trường hợp đơn giản nhất, một biểu thức Regex chỉ là một mẫu là chuỗi các ký tự dùng để tìm kiếm trong văn bản (chuỗi, text, string). Ví dụ một biểu thức RegEx `ước`, thì phù hợp với nó là bắt đầu bằng ư theo sau là ớ và tiếp theo là c, mang biểu thức đó so khớp với đoạn text (văn bản) thì thấy hợp mẫu như sau:
```
Hjx, `ước` gì có ny
```

thì sẽ có một so khớp `ước` trong văn bản.

## Các meta character

Các ký tự `meta` là các khối xây dựng của các biểu thức chính quy. Các ký tự `meta` không biểu diễn chính nó mà thay vào đó được diễn giải theo một cách đặc biệt nào đó. Một số ký tự `meta` có ý nghĩa đặc biệt và được viết bên trong dấu ngoặc vuông. Các ký tự meta như sau:

|Meta character|Description|
|:----:|----|
|.|Khớp với tất cả các kí tự trừ dấu xuống dòng.|
|[ ]|Lớp kí tự. Khớp với bất kỳ ký tự nào nằm giữa dấu ngoặc vuông.|
|[^ ]|Lớp kí tự phủ định. Khớp với bất kỳ ký tự nào không có trong dấu ngoặc vuông.|
|*|Khớp 0 hoặc nhiều lần lặp lại của kí tự trước.|
|+|Khớp 1 hoặc nhiều lần lặp lại của kí tự trước.|
|?|Làm cho kí tự trước tùy chọn.|
|{n,m}|Braces. Khớp ít nhất là "n" nhưng không nhiều hơn "m" lặp lại của kí tự trước.|
|(xyz)|Nhóm kí tự. Khớp các ký tự xyz theo thứ tự chính xác đó.|
|&#124;|Thay thế. Khớp các ký tự trước hoặc ký tự sau ký hiệu.|
|&#92;|Thoát khỏi kí tự tiếp theo. Điều này cho phép bạn khớp các ký tự dành riêng <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Khớp với sự bắt đầu của đầu vào.|
|$|Khớp với kết thúc đầu vào.|


### Dot

Dot `.` là một kí tự meta đơn giản. Nó đại diện cho bất kì kí tự nào ngoài trừ xuống dòng `newline \n`. Ngoài ra trong Python nếu ta dùng `DOTALL` thì nó sẽ mặc định khớp với cả xuống dòng `\n`. 
Ví dụ:
```python
import re
pattern=r".+"
text="Test1\rTest2\nTest3"
matches = re.findall(pattern, text)
print(matches)
matches_dotall = re.findall(pattern, text, re.DOTALL)
print(matches_dotall)
```
![image](https://github.com/user-attachments/assets/e9a18969-5f87-4bec-86ed-d45b582a3313)

Ở trường hợp đầu tiên thì nó không khớp với `\n` nên text được chia ra làm 2, còn ở trường hợp ta sử dụng `DOTALL` thì nó sẽ tính luôn cả `\n`

### Caret
Caret `^` khi xuất hiện ở đầu một biểu thức chính quy thì nó quy định rằng mẫu phải khớp với phần đầu của chuỗi.
Ví dụ:
```python
import re
pattern=r"^Hello World"
text1="Hello World, Im GPT"
text2="Hello, Im GPT"
match1=re.match(pattern,text1)
match2=re.match(pattern,text2)
print(bool(match1)) # True
print(bool(match2)) # False
```
Còn trong trường hợp ta muốn so khớp nhiều dòng ở một chuỗi nhiều dòng thì ta dùng flag `re.MULTILINE`

### $
Trong biểu thức chính quy thì `$` được dùng để so khớp ở vị trí cuối chuỗi. Muốn so khớp nhiều dòng thì ta có thể dùng flag `re.MULTILINE` tương tự như với Caret. 
Ví dụ:
```python
import re
pattern=r'abc$'
text1="đây là một chuỗi kết thúc bằng abc"
text2="chuỗi này không kết thúc bằng abc đâu"
if re.search(pattern, text1):
    print("text1 khớp với mẫu.")
else:
    print("text1 không khớp với mẫu.")
if re.search(pattern, text2):
    print("text2 khớp với mẫu.")
else:
    print("text2 không khớp với mẫu.")
# text1 khớp với mẫu.
# text2 không khớp với mẫu.
```

### *, +, ?
Kí tự meta `*` biểu thị việc lặp lại kí tự hoặc nhóm kí tự đứng trước nó ít nhất là 0 lần. Tức là nó có thể là chuỗi rỗng. 

Ví dụ: `0*` khớp với `" ","0","000"`. Còn `ab*` khớp với `"a","ab","abbbbb"`
```python
import re
pattern = r'ab*c'
text = "ac abc abbc abbbc"
matches = re.findall(pattern, text)
print(matches)
# ['ac', 'abc', 'abbc', 'abbbc']
```

Khác với `*` thì kí tự meta `+` biểu thị việc lặp lại kí tự hoặc nhóm kí tự đứng trước nó ít nhất là 1 lần, tức là chuỗi rỗng sẽ không so khớp được. 
```python
import re
pattern = r'ab+c'
text = "ac abc abbc abbbc"
matches = re.findall(pattern, text)
print(matches)
# ['abc', 'abbc', 'abbbc']
```
Tiếp theo là `?` biểu thị việc lặp lại kí tự hoặc nhóm kí tự đứng trước nó 0 hoặc 1 lần. Ví dụ với `colou?r` thì sẽ khớp với `color` hoặc `colour` nhưng không khớp với `colouur`. 
```python
import re
pattern = r'colou?r'
text = 'color, colour, colouur.'
matches = re.findall(pattern, text)
print(matches)
# ['color', 'colour']
```
### *?, +?, ??
Các kí tự meta `+`,`*` và `?` ban đầu đều ở chế độ tham lam (greedy mode) tức là chúng sẽ so khớp với càng nhiều kí tự càng tốt. Việc thêm kí tự `?` sẽ giúp chuyển về mode non-greedy tức là sẽ lấy so khớp ít nhất có thể có. 
Chẳng hạn 

```python=
import re
text='abbbbc'
pattern_greedy = r'ab*'
pattern_non_greedy = r'ab*?'
match_greedy = re.search(pattern_greedy, text)
match_non_greedy = re.search(pattern_non_greedy, text)
print(match_greedy.group())      # Output: 'abbbb'
print(match_non_greedy.group())  # Output: 'a'
```
Tương tự với `+?` và `??`


   
