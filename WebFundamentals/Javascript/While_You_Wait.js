var daystell = 60;
birthday(daystell);
function birthday(daystell){
    while (daystell > 0){
        if (daystell>=30){
            console.log(daystell, "days until my birthday. Such a long time...:(")
            daystell = daystell-1;
        }
        else if (daystell<30){
            if (daystell<=5){
                console.log(daystell, "DAYS TELL MY BIRTHDAY!!!")
                daystell = daystell-1;
            }
            else{
                console.log(daystell, "days tell my birthday. Getting Close!")
                daystell = daystell-1;
            }
        }
    }
    console.log("ITS MY BIRTHDAY!!")
}