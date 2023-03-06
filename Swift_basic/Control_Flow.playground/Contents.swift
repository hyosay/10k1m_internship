var isDarkMode : Bool = true

if (isDarkMode == true){
    print("this is darkmode")
} else{
    print("not darkmode")
}


var myarray : [Int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in myarray {
    print("item \(item)")
}


for item in myarray where item > 5 {
    print("over 5 item : \(item)")
}


// enum
enum School {
    case elementary
    case middle
    case high
    
    //or
    // case elementary, middle, high
}

let yourSchool = School.elementary
print("yourschool : \(yourSchool)")

enum Grade : Int {
    case first = 1
    case second = 2
}

let yourGrade = Grade.first
print("yourGrade: \(yourGrade.rawValue)")



enum SchoolDetail {
    case elementary(name: String)
    case middle(name: String)
    case high(name: String)
    
    func getName() -> String {
        switch self {
        case .elementary(let name):
            return name
        case let .middle(name):
            return name
        case let .high(name):
            return name
        }
    }
}

let yourMiddleSchoolname = SchoolDetail.middle(name: "삼성현중학교")

print("yourMiddleSchoolname: \(yourMiddleSchoolname)")
print("yourMiddleSchoolname: \(yourMiddleSchoolname.getName())")

enum expressions {
    case number(Int)
    indirect case addition(expressions, expressions)
    indirect case multiplication(expressions, expressions)
}

let five = expressions.number(5)
let six = expressions.number(6)
let sum = expressions.addition(five, six)
let product = expressions.multiplication(sum, expressions.number(2))

func evalute(_ expression: expressions) -> Int {
    switch expression {
    case let .number(value):
        return value
    case let .multiplication(left, right):
        return evalute(left) * evalute(right)
    case let .addition(left, right):
        return evalute(left) + evalute(right)
    }
}

print(evalute(product))


// for 문


for i in 0...5 {
    print("number i:v\(i)")
}

for index in 0...10 where index % 2 == 0 {
    print("index : \(index)")
}


var RandomInts: [Int] = []


// optional

var someVariable : Int? = 5


print(someVariable)

let myvalue = someVariable ?? 10

print(myvalue)
//if let otherVariable = myvalue {
//    print("unwrapping, and true variable \(myvalue)")
//} else {
//    print("non variable")
//}
//


func printName() {
    var name: String?
    name = "hyosay"
    print(name)
    
    guard let myName = name else { return }
    print(myName)
}
printName()


var firstNumber: Int? = nil
print(firstNumber)

if let checkNumber = firstNumber {
    print(checkNumber)
}




// struct


struct MemberInfomation {
    var name: String
    var age: Int
}

var firstMember = MemberInfomation(name: "hyosay", age: 25)

var secondMember = firstMember

print(secondMember.name)

secondMember.name = "hyoseong jeon"
print(secondMember.name)

//class

class MemberInfomationClass {
    var name: String
    var age : Int
    
    //생성자 - 즉 메모리에 올린다.
    //init 으로 매개변수를 가진 생성자 메소드를 만들어야
    //매개변수를 넣어서 그값을 가진 객체(object)를 만들 수 있다.
    init(name: String, age: Int){
        self.name = name
        self.age = age
    }
}

var threeMember = MemberInfomationClass(name: "jinja", age: 26)


