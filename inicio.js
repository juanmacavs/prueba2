

let bandera = false;
let turno = 0;
let tab = new Array();
window.onload = function(){ 
    let iniciar = document.getElementById("iniciar");
    iniciar.addEventListener("click",comenzar);
}
function comenzar(){
    bandera = true;
    
    let jugador1 = document.getElementById("jugador1")
    console.log (jugador1.value)

    let jugador2 = document.getElementById("jugador2");
    
    if(jugador1.value== ""){
        alert("Falta el nombre del Jugador 1");
        jugador1.focus();
    }else{
        if(jugador2.value==""){
            alert("Falta el nombre del jugador 2")
            jugador2.focus();
        }else{
            tab [1] = document.getElementById("b1");
            tab [2] = document.getElementById("b2");
            tab [3] = document.getElementById("b3");
            tab [4] = document.getElementById("b4");
            tab [5] = document.getElementById("b5");
            tab [6] = document.getElementById("b6");
            tab [7] = document.getElementById("b7");
            tab [8] = document.getElementById("b8");
            tab [9] = document.getElementById("b9");
            for(let i=0;i<0;i++){
                tab[i].className = "botonInicial";
                tab[i].value = "I"
            }
            turno = 1;
            document.getElementById("turnoJugador").innerHTML =
            "Adelante Jugador " + jugador1.value;
        }
    }
}
funcion colocar(boton){
    if(bandera==true){
        if(turno==1 && boton.value=="I"){
            turno = 2;
            document.getElementById("turnoJugador").innerHTML =
            "Adelante Jugador" + jugador2.value;
            boton.value = "X";
            boton.className = "jugador1"

        }
    }
}    