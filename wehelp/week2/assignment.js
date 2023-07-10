console.log("=== Task 1 ===")
function findAndPrint(messages){
    // write down your judgment rules in comments
    // your code here, based on your own rules
    const keywords = ["18 years old", "college student", "legal age", "vote"];
    for(var name in messages){
        for(var key in keywords){
            // console.log(keywords[key])
            if(messages[name].includes(keywords[key])){
                console.log(name);
            }
        }
    }
}
findAndPrint({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
});

console.log("=== Task 2 ===")
function calculateSumOfBonus(data){
    // write down your bonus rule in comments
    // your code here, based on your own rules

    // bonus rule:
    // performance bonus ratio "above average" : 5%
    // performance bonus ratio "average": 3%
    // performance bonus ratio "below average": 1%

    // role bonus ratio "Engineer": 5%
    // role bonus ratio "Sales": 3%
    // role bonus ratio "CEO": 1%

    // The bonus of each staff is: Math.min(salary * (performance ratio + role ratio), 2500)
    var total_bonus = 0;
    for(i in data["employees"]){
        var salary = data["employees"][i]["salary"];
        var performance = data["employees"][i]["performance"];
        var role = data["employees"][i]["role"];
        var bonus_ratio = 0;

        if (performance == "above average") {
            bonus_ratio += 0.05;
        } else if (performance == "average") {
            bonus_ratio += 0.03;
        } else if (performance == "below average") {
            bonus_ratio += 0.01;
        }
        
        if (role == "Engineer") {
            bonus_ratio += 0.05;
        } else if (role == "Sales") {
            bonus_ratio += 0.03;
        } else if (role == "CEO") {
            bonus_ratio += 0.01;
        }

        if (typeof salary === "string"){
            if (salary.includes("USD")){
                data["employees"][i]["salary"] = parseInt(salary.replace(/USD/, "")) * 30;
            }else if (salary.includes(",")){
                data["employees"][i]["salary"] = parseInt(salary.replace(/,/, ""));
            }
        }

        data["employees"][i]['bonus'] = Math.min(data["employees"][i]["salary"] * bonus_ratio, 2500);
        
        total_bonus += data["employees"][i]['bonus'];
    }
    console.log(total_bonus);
}
calculateSumOfBonus({
"employees":[
{
"name":"John",
"salary":"1000USD",
"performance":"above average",
"role":"Engineer"
},
{
"name":"Bob",
"salary":60000,
"performance":"average",
"role":"CEO"
},
{
"name":"Jenny",
"salary":"50,000",
"performance":"below average",
"role":"Sales"
}
]
}); // call calculateSumOfBonus function

console.log("=== Task 3 ===")
function func(...data){
    // your code here
    var temp = {};
    data.forEach(function(name) {
        temp[name[1]] = temp[name[1]] || [];
        temp[name[1]].push(name);
    });
    for (i in temp){
        if (temp[i].length == 1){
            console.log(temp[i][0]);
            return;
        }
    }
    console.log("沒有");
}
func("彭大牆", "王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有

console.log("=== Task 4 ===")
function getNumber(index){
    // your code here
    if (index >= 0){
        var ret = (Math.floor((index + 1) / 2) * 4) - Math.floor(index / 2);
        console.log(ret);
    }
}
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15

console.log("=== Task 5 ===")
function findIndexOfCar(seats, status, number){
    // your code here
    var ret = {};
    var car = null;
    for (i in status){
        if (status[i] == 1){
            if (seats[i] >= number){
                ret[i] = seats[i] - number;
            }
        }
    }
    if (Object.keys(ret).length === 0) {
        car = -1;
    } else {
        car = Object.keys(ret).reduce(function(a, b) {
            return ret[a] < ret[b] ? a : b;
        });
    }
    console.log(car)
}
findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4
findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2