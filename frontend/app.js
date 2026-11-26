"use strict";
const series = {"24": [38,39,42,45,44,43,42,42], "7": [35,48,40,51,43,46,42]};
const chart = document.querySelector("#chart");
const period = document.querySelector("#period");
const ns = "http://www.w3.org/2000/svg";
function draw(){
 const values = series[period.value];
 chart.replaceChildren();
 for(const tick of [0,25,50,75,100]){
  const y=150-tick*1.3;
  const line=document.createElementNS(ns,"line");
  for(const [k,v] of Object.entries({x1:40,x2:580,y1:y,y2:y,stroke:"#364451"})) line.setAttribute(k,v);
  chart.append(line);
  const label=document.createElementNS(ns,"text");label.setAttribute("x","4");label.setAttribute("y",y+4);label.setAttribute("fill","#aab5c1");label.setAttribute("font-size","12");label.textContent=tick+"%";chart.append(label);
 }
 const path=document.createElementNS(ns,"polyline");
 path.setAttribute("points",values.map((v,i)=>[40+i*540/(values.length-1),150-v*1.3].join(",")).join(" "));
 path.setAttribute("fill","none");path.setAttribute("stroke","var(--accent)");path.setAttribute("stroke-width","3");path.setAttribute("stroke-linejoin","round");chart.append(path);
 document.querySelector("#summary").textContent="Simulated range: "+Math.min(...values)+"–"+Math.max(...values)+"%.";
}
period.addEventListener("change",draw);draw();
