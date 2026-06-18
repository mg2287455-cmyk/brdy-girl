from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Happy Birthday Ashisha</title>

<style>

body{
    background:linear-gradient(135deg,#ffb6c1,#ffd6e0);
    font-family:Arial,sans-serif;
    text-align:center;
    padding:50px;
    overflow-x:hidden;
}

.card{
    background:white;
    max-width:700px;
    margin:auto;
    padding:30px;
    border-radius:20px;
    box-shadow:0 0 20px rgba(0,0,0,0.2);
}

h1{
    color:#e91e63;
}

button{
    padding:12px 25px;
    font-size:18px;
    border:none;
    border-radius:10px;
    background:#e91e63;
    color:white;
    cursor:pointer;
}

#message{
    margin-top:25px;
    font-size:20px;
    line-height:1.8;
}

.fall{
    position:fixed;
    top:-50px;
    animation:fall 5s linear forwards;
}

@keyframes fall{
    from{transform:translateY(-100px);}
    to{transform:translateY(110vh);}
}

.sparkle{
    position:fixed;
    animation:spark 3s linear forwards;
}

@keyframes spark{
    from{
        transform:translateY(0px) scale(0.5);
        opacity:1;
    }
    to{
        transform:translateY(-250px) scale(1.5);
        opacity:0;
    }
}

.popup{
    position:fixed;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    background:white;
    color:#e91e63;
    padding:20px 30px;
    border-radius:15px;
    font-size:28px;
    font-weight:bold;
    box-shadow:0 0 25px rgba(0,0,0,0.3);
    z-index:9999;
}

</style>
</head>

<body>

<div class="card">

<h1>🎂 Happy Birthday Ashisha 🎂</h1>

<p>
Wishing you a wonderful day filled with happiness and smiles.
</p>

<button onclick="showWish()">
Open Birthday Wish
</button>

<div id="message"></div>

</div>

<script>

function showWish(){

// Popup
let pop=document.createElement("div");

pop.className="popup";

pop.innerHTML="🎂 Happy Birthday Ashisha 🎂";

document.body.appendChild(pop);

setTimeout(()=>{
    pop.remove();
},3000);


// Message
document.getElementById("message").innerHTML=`

<p>

❤️ Happy Birthday Ashisha ❤️

<br><br>

May your life be filled with happiness,
success and beautiful memories.

Keep smiling and enjoy your special day.

I wish you all the best for your future. 🌹🎂

</p>

<h3>💌 From Monu</h3>

`;


// Roses
for(let i=0;i<40;i++){

let flower=document.createElement("div");

flower.innerHTML="🌹🎂";

flower.className="fall";

flower.style.left=Math.random()*1000+"vw";

flower.style.fontSize=(20+Math.random()*20)+"px";

document.body.appendChild(flower);

setTimeout(()=>{
flower.remove();
},5000);

}


// Sparkles
for(let i=0;i<60;i++){

let star=document.createElement("div");

star.innerHTML="✨";

star.className="sparkle";

star.style.left=Math.random()*100+"vw";

star.style.top=Math.random()*100+"vh";

star.style.fontSize=(15+Math.random()*20)+"px";

document.body.appendChild(star);

setTimeout(()=>{
star.remove();
},3000);

}

}

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True ,port=50199)