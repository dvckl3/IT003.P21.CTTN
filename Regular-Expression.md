# Thư viện Regular Expression trong Python


## Khái niệm biểu thức chính quy 
Biểu thức chính quy là các mẫu dùng để tìm kiếm các bộ kí tự được kết hợp với nhau trong các chuỗi kí tự. Các nhóm kí tự, kí hiệu được viết ra theo quy luật tạo thành mẫu và nó được sử dụng để tìm kiếm văn bản.

Một biểu thức chính quy là một mẫu (pattern) nó tương đồng quy luật với một chuỗi từ trái qua phải. 
Trong Python3 có thư viện `re` hỗ trợ làm việc với biểu thức chính quy. Doc đầy đủ về thư viện này có thể tham khảo tại [đây](https://docs.python.org/2/library/re.html#module-re). 

![image](https://github.com/user-attachments/assets/3d9b08fc-ddba-4055-a33e-ec460f244551)

## Một số cú pháp Python

| Hàm                      | Mô tả                                                                 |
|--------------------------|-----------------------------------------------------------------------|
| `re.match(pattern, string)` | Kiểm tra xem phần đầu của chuỗi có khớp với mẫu không. Trả về đối tượng match nếu khớp, ngược lại trả về `None`. |
| `re.search(pattern, string)` | Tìm kiếm mẫu trong toàn bộ chuỗi. Trả về đối tượng match của lần xuất hiện đầu tiên nếu tìm thấy, ngược lại trả về `None`. |
| `re.findall(pattern, string)` | Tìm tất cả các lần xuất hiện của mẫu trong chuỗi và trả về danh sách các chuỗi khớp. |
| `re.finditer(pattern, string)` | Tương tự như `findall`, nhưng trả về một iterator chứa tất cả các đối tượng match. |
| `re.sub(pattern, repl, string)` | Thay thế tất cả các phần khớp với mẫu trong chuỗi bằng chuỗi thay thế `repl`. |
| `re.split(pattern, string)` | Tách chuỗi thành danh sách các phần tử dựa trên mẫu. |
| `re.compile(pattern)` | Tiền biên dịch mẫu regex để sử dụng nhiều lần, giúp tăng hiệu suất. |



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

```python
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

### {m}, {m,n}, {m,n}?
`{m}` biểu thị việc lặp lại kí tự hoặc nhóm kí tự đứng trước nó đúng $m$ lần. Nếu ít hơn $m$ thì sẽ không so khớp. Chẳng hạn như `a{6}` thì sẽ so khớp với `aaaaaa`.


`{m,n}` khớp từ `m` đến `n`  kí tự, hoặc nhóm kí tự đướng trước nó. Ví dụ `a{2,4}` thì sẽ so khớp với `aa,aaa,aaaa`. Mode greedy thì sẽ lấy nhiều nhất có thể. Ngoài ra nếu ta bỏ `m` đi thì lower bound của số kí tự là 0, `{,n}`, cón nếu bỏ `n` đi thì upper bound của số kí tự sẽ là vô hạn, tức là bao nhiêu cũng được, `{m,}`

`{m,n}?`, như ta đã đề cập ở trên thì việc thêm kí tự `?` sẽ đưa meta char về non greedy mode, tức là lấy ít nhất có thể, ví dụ `aaaaa` thì khi dùng so khớp `a{2,4}` sẽ chỉ trả về `aa`.

Ví dụ:

```python
import re

# Chuỗi mẫu
text = "aaaaa"

# Sử dụng {m}
pattern1 = r'a{3}'
match1 = re.search(pattern1, text)
print(match1.group())  # Output: 'aaa'

# Sử dụng {m,n} (tham lam)
pattern2 = r'a{2,4}'
match2 = re.search(pattern2, text)
print(match2.group())  # Output: 'aaaa'

# Sử dụng {m,n}? (không tham lam)
pattern3 = r'a{2,4}?'
match3 = re.search(pattern3, text)
print(match3.group())  # Output: 'aa'
```
### |, `\`, []
`\` dùng để biểu diễn các kí tự đặc biệt, cụ thể nó được dùng để thoát các kí tự đặc biệt. Chẳng hạn ta có `\.` sẽ so khớp với dấu chấm `.` trong văn bản thay vì meta char Dot như ta đề cập ở trên. 

`|` hay OR dùng để so khớp với nhiều lựa chọn biểu thức chính quy khác nhau. Ví dụ `A|B` sẽ match với một trong hai REs `A` hoặc `B` và sẽ so khớp từ trái sang phải, tức là kiểm tra `A` trước rồi mới tới `B`.

Cuối cùng và quan trọng nhất là ngoặc vuông `[]` dùng để chỉ một tập hợp các kí tự có thể so khớp tại một vị trí cụ thể.

Ví dụ: `[a-zA-Z]` sẽ khớp với bất kì chữ cái nào, không phân biệt chữ hoa hay thường. 

```python
import re
text = "Thời gian: 10.30 sáng."
pattern = r'\d+\.\d+'
matches = re.findall(pattern, text)
print(matches)
# ['10.30']
```

```python
import re
text = "Tôi có một con mèo và một con chó."
pattern = r'mèo|chó'
matches = re.findall(pattern, text)
print(matches)
# ['mèo', 'chó']
```


```python
import re
text = "abc xyz acb bac cab"
pattern = r'[abc]'
matches = re.findall(pattern, text)
print(matches)
# ['a', 'b', 'c', 'a', 'c', 'b', 'b', 'a', 'c', 'c', 'a', 'b']
```

### Capturing group and Non-capturing group


| Loại nhóm            | Cú pháp      | Mô tả                                                                                 |
|----------------------|--------------|---------------------------------------------------------------------------------------|
| Capturing Group      | `(pattern)`  | Nhóm biểu thức và lưu trữ phần khớp để truy xuất sau này.                             |
| Non-Capturing Group  | `(?:pattern)`| Nhóm biểu thức mà không lưu trữ phần khớp, hữu ích khi không cần truy xuất nội dung.   |


```python
import re

s = 'Python 3.10'
pattern = r'(\d+)\.(\d+)'

match = re.search(pattern, s)
if match:
    print(match.group())   # Output: 3.10
    print(match.group(1))  # Output: 3
    print(match.group(2))  # Output: 10
```

Capturing groups cho phép ta nhóm một phần của biểu thức chính quy và trích xuất nội dung khớp với phần đó. Để tạo một capturing group, ta đặt phần biểu thức cần nhóm trong dấu ngoặc đơn `()`. Khi một biểu thức chính quy với capturing groups khớp với một chuỗi, ta có thể truy xuất nội dung của các nhóm này thông qua phương thức `.group()` của đối tượng match.

Còn ở ví dụ dưới đây, `(?:\d+)` là non-capturing group, khớp với phần `3` nhưng không lưu trữ nội dung.
```python
import re

s = 'Python 3.10'
pattern = r'(?:\d+)\.(\d+)'

match = re.search(pattern, s)
if match:
    print(match.group())   # Output: 3.10
    print(match.group(1))  # Output: 10
```

## Shorthand Character Sets
Biểu thức chính quy cung cấp các shorthand cho các bộ ký tự thường được sử dụng, cung cấp các shorthand thuận tiện cho các biểu thức thông thường được sử dụng. Các bộ ký tự shorthand như sau:


| Shorthand | Mô tả                                                                                             | Biểu thức tương đương     |
|-----------|---------------------------------------------------------------------------------------------------|---------------------------|
| `\d`      | Bất kỳ chữ số nào từ 0 đến 9                                                                       | `[0-9]`                   |
| `\D`      | Bất kỳ ký tự nào không phải là chữ số                                                              | `[^0-9]`                  |
| `\w`      | Bất kỳ ký tự chữ cái, chữ số hoặc dấu gạch dưới                                                     | `[a-zA-Z0-9_]`            |
| `\W`      | Bất kỳ ký tự nào không phải là chữ cái, chữ số hoặc dấu gạch dưới                                   | `[^a-zA-Z0-9_]`           |
| `\s`      | Bất kỳ ký tự khoảng trắng nào (khoảng trắng, tab, xuống dòng, v.v.)                                | `[ \t\n\r\f\v]`           |
| `\S`      | Bất kỳ ký tự nào không phải là khoảng trắng                                                        | `[^ \t\n\r\f\v]`          |
| `\b`      | Khớp với vị trí nằm giữa một ký tự thuộc nhóm `\w` và một ký tự không thuộc nhóm `\w` (ranh giới từ) |                           |
| `\B`      | Khớp với vị trí không phải là ranh giới từ                                                         |                           |

## Flags


Cờ (flags) cũng được gọi là bổ nghĩa (modifiers) vì chúng sửa đổi đầu ra của biểu thức chính quy. Các cờ này có thể được sử dụng theo bất kỳ thứ tự hoặc kết hợp nào và là một phần không thể thiếu của RegExp. Trong Python có các cờ như sau: 



| Cờ (Flag)       | Tên viết tắt | Mô tả                                                                                     |
|-----------------|--------------|-------------------------------------------------------------------------------------------|
| `re.IGNORECASE` | `re.I`       | Không phân biệt chữ hoa và chữ thường khi so khớp.                                         |
| `re.MULTILINE`  | `re.M`       | Cho phép các ký tự mỏ neo như `^` và `$` khớp với vị trí bắt đầu và kết thúc của mỗi dòng.|
| `re.DOTALL`     | `re.S`       | Làm cho ký tự `.` khớp với tất cả các ký tự, bao gồm cả ký tự xuống dòng (`\n`).           |
| `re.VERBOSE`    | `re.X`       | Cho phép viết biểu thức chính quy trên nhiều dòng và thêm chú thích, giúp biểu thức dễ đọc hơn.|
| `re.ASCII`      | `re.A`       | Buộc các ký tự đặc biệt như `\w`, `\b`, `\s` chỉ khớp với các ký tự ASCII.                 |
| `re.UNICODE`    | `re.U`       | Đây là giá trị mặc định; các ký tự đặc biệt sẽ khớp với cả các ký tự Unicode.              |
| `re.LOCALE`     | `re.L`       | Sử dụng cài đặt ngôn ngữ địa phương (locale) để xác định hành vi của các ký tự đặc biệt.   |




(Still updating...)
