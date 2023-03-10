# value type과 Reference Type
> 스위프트 공부를 하던 도중 값타입, 참조타입 이 두단어가 계속 언급되었다.     



c언어를 처음 배웠을 떄 포인트(\*)에 대한 학습을 했던 기억이 있다.

```c++
int a;
int &ta = a;
```

이런식으로 값을 직접적으로 복사하는 것이 아닌 주소를 복사(?)하는 것이었다.   
프로그래밍을 입문하였던 나는 이해가 되지 않았다 copy한 변수의 값을 변경하였는데 기존에 있던 값까지 변경이 되었던 것이다.
> 프로그래밍을 포기할려고 했다..

## value type

값타입(value)에 대해서 내가 이해한것을 토대로 정리해보겠다.

**"struct" and "enum" is ValueType**

```swift
struct Student {
  var name: String
  var age: Int
}

var std1 = Student(name: "hyosay", age: 25)
var std2 = st1

std2.name = "hyoseong"
//Prints std1.name "hyosay", std2.name "hyoseong"
```
 위 결과와 같이 값을 복사한 후 std2.name의 값을 변경하여도 std1의 정보는 변화지 않았다.   
 
 
 
 즉 결론적으로 카카오톡을 보내는 것을 예시로 들면 된다 .   
 본인의 로컬에 있는 이미지, 동영상 파일을 공유하고, 공유받은 사람이 편집을 진행하여도 내가 가지고 있는 파일의 원본이 남아있다. = Value Type   
 하지만 링크를 통해서 파일을 공유하였을 떄는, 링크 안에 있는 파일을 수정하면 내용이 전체적으로 바뀐다. -> Reference Type
 
