use s2::greet;
fn main() {
    shadow();
    memory_safety_init_var();
    greet();
    tuple_example();
    if_example(5);
}
fn shadow() {
    let x = 10;
    {
        let x = 20;
        println!("{}", x); // 20
    }
    println!("{}", x); // 10
}

fn memory_safety_init_var(){
    let mut enigma: i32;
    // println!("{}", enigma); // wont work
    if true {
        enigma = 3;
        println!("{}", enigma);
    } else {
        enigma = 7;
    }
    println!("{}", enigma); // error if not else block before build rust saves day 
}

fn tuple_example(){
    let info:(u8,f64,i32) = (1,2.3,4);
    println!("{} {} {}",info.0,info.1,info.2);
    // let jets= info.0;
    // let fuel = info.1;
    // let age = info.2;
    // println!("{} {} {}",jets,fuel,age);
    let (jets,fuel,ammo)=info;
    println!("jets:{} fuel:{} ammo:{}",jets,fuel,ammo);
}

fn array_example(){
    let arr = [1,2,3,4,5];
    println!("{}",arr[0]);
    let arr2 = [3;5]; // [3,3,3,3,3]
    println!("{}",arr2[0]);
}

fn if_example (num:i32){
    let msg = if num ==5 {
        "five"
    } else if num==4{
        "four"
    } else {
        "other"
    };
    println!("{}",msg);
}
fn loop_example() {
    for i in 1..=5 {
        println!("{}",i);
    }
}

