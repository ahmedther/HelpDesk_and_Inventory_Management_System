(()=>{var e,o,r;e=document.querySelector(".error"),setTimeout((function(){return e.remove()}),12e3),o=document.querySelector(".progressbar"),r=document.body.scrollHeight-window.innerHeight,window.onscroll=function(){var e=window.pageYOffset/r*100;o.style.height=e+"%"}})();