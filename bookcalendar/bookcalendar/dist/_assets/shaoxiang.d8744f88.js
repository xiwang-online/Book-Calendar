let t=document.createElement("style");t.innerHTML=".index[data-v-0ba017ec]{width:100%;height:100%}#container[data-v-0ba017ec]{transform:translate(0,-80px)}.note[data-v-0ba017ec]{width:500px;height:150px;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);border:4px solid #fff}.f[data-v-0ba017ec]{font-size:24px;margin:25px;color:#cecece}.b1[data-v-0ba017ec]{position:absolute;bottom:15px;right:100px}.b2[data-v-0ba017ec]{position:absolute;bottom:15px;right:25px}",document.head.appendChild(t);import{r as e,o as a,a as n,u as i,b as o,c as s,d as l,k as p,v as c,e as r,g as m,w as d,f as u,F as f,i as x,p as v,l as b,j as g}from"./index.82c7254e.js";var h={name:"test2",props:[],setup(){const t=i(),s=o();let l=e({center:{x:250,y:250},spiralExpanse:8,pointnum:550,points:[],animationFrame:!0,display:0});function p(){!function(){let e=!1;for(let t=1;t<l.points.length;t++){let a=l.points[t],n=l.mouseX-a.x,i=l.mouseY-a.y,o=Math.sqrt(n*n+i*i);!0===l.points[t].active&&(e=!0),o<25&&!0===l.points[t].active?(l.points[t].life=l.points[t].life-.04,l.points[t].life<=0&&(l.points[t].active=!1)):!0===l.points[t].active&&l.points[t].life<1&&(l.points[t].life=l.points[t].life+.05)}!1===e&&(cancelAnimationFrame(l.animationFrame),l.animationFrame=null,alert("烧香结束，恭喜获得1000点功德！"),t.commit("gd",1e3),window.localStorage.setItem("muyutime",t.state.gongde),s.push("/"))}(),l.animationFrame&&(!function(){var t=document.getElementById("container");if(t.getContext){var e=t.getContext("2d");e.clearRect(0,0,500,500),e.lineCap="round",e.moveTo(l.points[0].x,l.points[0].y);for(let t=1;t<l.points.length;t++)l.points[t].life<1&&!0===l.points[t].active?e.strokeStyle="rgba(244, 110, 28, "+(.1+l.points[t].life)+")":e.strokeStyle="rgba(255, 255, 255, "+(.1+l.points[t].life)+")",e.lineWidth=6*l.points[t].life+4+"",e.beginPath(),e.moveTo(l.points[t-1].x,l.points[t-1].y),e.lineTo(l.points[t].x,l.points[t].y),e.stroke()}}(),l.animationFrame=requestAnimationFrame(p))}return a((()=>{})),n((()=>{cancelAnimationFrame(l.animationFrame),l.animationFrame=null})),{data:l,mousepos:function(t){l.mouseX=t.offsetX,l.mouseY=t.offsetY},cal:function(){s.push("/")},yes:function(){l.display=1,t.commit("gd",-500),window.localStorage.setItem("muyutime",t.state.gongde),function(){for(let t=0;t<l.pointnum;t++){let e={},a=.05*-t;e.x=l.center.x+l.spiralExpanse*a*Math.cos(a),e.y=l.center.y+l.spiralExpanse*a*Math.sin(a),e.active=!0,e.life=1,l.points.push(e)}}(),p()}}}};const y={class:"index"},F={key:0,class:"note"},k=(t=>(v("data-v-0ba017ec"),t=t(),b(),t))((()=>r("div",{class:"f"},"烧香将花费500功德，烧完可得1000功德，确定要烧香吗？",-1))),w=g("取消"),C=g("确定");h.render=function(t,e,a,n,i,o){const v=x("el-button");return s(),l(f,null,[p(r("div",y,[r("canvas",{id:"container",width:"500",height:"500",onMousemove:e[0]||(e[0]=(...t)=>n.mousepos&&n.mousepos(...t))},null,32)],512),[[c,n.data.display]]),n.data.display?u("",!0):(s(),l("div",F,[k,m(v,{class:"b1",onClick:n.cal},{default:d((()=>[w])),_:1},8,["onClick"]),m(v,{class:"b2",onClick:n.yes,type:"primary",plain:""},{default:d((()=>[C])),_:1},8,["onClick"])]))],64)},h.__scopeId="data-v-0ba017ec";export{h as default};