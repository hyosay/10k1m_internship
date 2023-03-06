import UIKit

class MemberInformation {
    var name : String
    var age : Int
    var weight : Int
    var height : Int
    
    init(name: String, age: Int, weight: Int, height: Int) {
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    }
}

var first = MemberInformation(name: "hyosay", age: 25, weight: 100, height: 180)
// class copy

var second = first

//before
print("first name: \(first.name)")
print("second name: \(second.name)")


//rename secondMember
second.name = "hyoseong_j"


//after
print("first name: \(first.name)")
print("second name: \(second.name)")

// Class statements are Linked together
