var hr=6;
var min=30;
var period="PM"
time(hr,min,period)

function time(hr,min,period){
    if (period=="AM"){
        if (hr==12 && min==0){
            console.log("Its midnight")
        }
        else if (min==30){
            console.log("Its half past", hr ,"in the morning.")
        }
        else if (min<30){
            if (min==5){
                console.log("Its five after", hr, "in the morning")
            }
            else if (min==15){
                console.log("Its a quarter after", hr, "in the morning")
            }
            else{
                console.log("Its just after", hr, "in the morning")
            }
        }
        else if (min>30){
            if (min==45){
                console.log("Its quarter tell", hr+1, "in the morning")
            }
            else{
                console.log("Its almost", hr+1, "in the morning")
            }
        }  
    }
    else if(period=="PM"){
        if (hr==12 && min==0){
            console.log("Its noon");
        }
        else if (hr<5){
            if (min==30){
                console.log("Its half past", hr ,"in the afternoon.");
            }
            else if (min<30){
                if (min==5){
                    console.log("Its five after", hr, "in the afternoon");
                }
                else if (min==15){
                    console.log("Its a quarter after", hr, "in the afternoon");
                }
                else{
                    console.log("Its just after", hr, "in the afternoon")
                }
            }
            else if (min>30){
                    if (min==45){
                        console.log("Its quarter tell", hr+1, "in the afternoon")
                    }
                    else{
                        console.log("Its almost", hr+1, "in the afternoon")
                    }
            }
        }
        else if (hr>=5){
            if (min==30){
                console.log("Its half past", hr ,"at night.");
            }
            else if (min<30){
                if (min==5){
                    console.log("Its five after", hr, "at night")
                }
                else if (min==15){
                    console.log("Its a quarter after", hr, "at night")
                }
                else{
                    console.log("Its just after", hr, "at night")
                }
            }
            else if (min>30){
                if (min==45){
                    console.log("Its quarter tell", hr+1, "at night")
                }
                else{
                    console.log("Its almost", hr+1, "at night")
                }
            }
        }
    }
}
