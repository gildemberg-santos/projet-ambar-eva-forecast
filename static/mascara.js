function mascara(o,f){
    v_obj=o
    v_fun=f
    setTimeout("execmascara()",1)
}

function execmascara(){
    v_obj.value=v_fun(v_obj.value)
}

function data(v){
    v=v.replace(/\D/g,"")
    v=v.replace(/^(\d\d)(\d\d)(\d\d\d\d)/g,"$1/$2/$3")
    return v
}
