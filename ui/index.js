
// YARVIS DataFrame
var ydf = undefined

fetch("http://localhost:5000/api")
.then(response => response.json())
.then((data) => {
    console.log("this is a test: " + JSON.stringify(data))
    console.log('Success:', data);
    ydf = data
})
.catch((error) => {
    console.error('Error:', error);
});

MAX_CORE_HOURS = 100000;
MAX_SKILL_HOURS = 10000;

console.log(ydf);

function hrs_to_level(hrs, is_skill=false, is_total=false) {
    if(is_total){
        return 95 * (Math.log10((hrs/3) + 10000) - 4) + 1;
    }
    if(is_skill){
        return 95 * (Math.log10(hrs + 1000) - 3) + 1;
    }
    else {
        return 95 * (Math.log10(hrs + 10000) - 4) + 1;
    }
}

// Update User Information
for (const key in ydf["Info"]) {
    var element = document.getElementById(key);
    element.innerHTML = element.innerHTML.split(": ")[0] + ": " + String(ydf["Info"][key]);
}
var element = document.getElementById("Level");
total_hrs = ydf["Core"]["Health"]["Total"] + ydf["Core"]["Intelligence"]["Total"] + ydf["Core"]["Soul"]["Total"];
element.innerHTML = element.innerHTML.split(": ")[0] + ": Lvl " + String(parseInt(hrs_to_level(total_hrs, is_skill=false, is_total=true)));

// Update Progress Bars
//// Life Progress
for (const key in ydf["Core"]) {
    var element = document.getElementById(key);
    percentage = ydf["Core"][key]["Total"] / MAX_CORE_HOURS;
    level = parseInt(hrs_to_level(ydf["Core"][key]["Total"]));
    element.innerHTML = String(parseInt(percentage*100)) + "%";
    element.style.width = String(parseInt(percentage*100)) + "%";
    var element = document.getElementById(key + " Level")
    element.innerHTML = element.innerHTML.split(": ")[0] + ": Lvl " + String(level);
    //// Skills
    for (const skill in ydf["Core"][key]["Skill Tree"]) {
        var element = document.getElementById(skill);
        percentage = ydf["Core"][key]["Skill Tree"][skill]["Total"] / MAX_SKILL_HOURS;
        level = parseInt(hrs_to_level(ydf["Core"][key]["Skill Tree"][skill]["Total"], is_skill=true));
        element.innerHTML = String(parseInt(percentage*100)) + "%";
        element.style.width = String(parseInt(percentage*100)) + "%";
        var element = document.getElementById(skill + " Level")
        element.innerHTML = element.innerHTML.split(": ")[0] + ": Lvl " + String(level);
    }
}

// Pie Chart - Time Allocation
var xValues = [];
var yValues = [];
var barColors = [];

for (const key in ydf["Core"]) {
    total = 0.00001
    for (const skill in ydf["Core"][key]["Skill Tree"]) {
        xValues.push(skill);
        total = total + ydf["Core"][key]["Skill Tree"][skill]["Total"];
    }
    i = 0;
    for (const skill in ydf["Core"][key]["Skill Tree"]) {
        yValues.push(parseInt((ydf["Core"][key]["Skill Tree"][skill]["Total"]/total)*100)/100);
        i = i + 1;
        barColors.push("rgba(0,150,136," + parseInt((i/yValues.length)*100)/100 + ")");
    }
}

var ctx = document.getElementById("myPieChart").getContext("2d");
var myPieChart = new Chart(ctx, {
    type: "doughnut",
    data: {
    labels: xValues,
    datasets: [{
        backgroundColor: barColors,
        data: yValues
    }]
    },
    options: {
    title: {
        display: false,
        text: "World Wide Wine Production 2018"
    }
    }
});

// TODO Line Chart - Progress Chart
// For data interval in date interval query server and create dataset.
var xValues = [100,200,300,400,500,600,700,800,900,1000];

var ctx = document.getElementById("myLineChart").getContext("2d");
var myLineChart = new Chart(ctx, {
    type: "line",
    data: {
    labels: xValues,
    datasets: [{ 
        data: [860,1140,1060,1060,1070,1110,1330,2210,7830,2478],
        borderColor: "red",
        fill: false
    }, { 
        data: [1600,1700,1700,1900,2000,2700,4000,5000,6000,7000],
        borderColor: "green",
        fill: false
    }, { 
        data: [300,700,2000,5000,6000,4000,2000,1000,200,100],
        borderColor: "blue",
        fill: false
    }]
    },
    options: {
    legend: {display: false}
    }
});


// Script to open and close sidebar
// TODO add functions in side bar to change date
function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
}
    
function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
}

