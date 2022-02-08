// window.onscroll = function() {
//     if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
//   document.getElementById("smrat_navbar").classList.add('navbar-bg-color');
// } else {
//   document.getElementById("smrat_navbar").classList.remove('navbar-bg-color');
// }
// };



// code for cart item incress,decress and remove

// cart quantity plus
$(".plus-cart").click(function() {
    var id = $(this).attr("pid").toString() ;
    var eml = this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id : id  
        },
        success:function(data){
            eml.innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
            document.getElementsByClassName('pro_amount').innerText = data.pro_amount
        }
    })
    
});
// cart quantity minus
$(".minus-cart").click(function() {
    var id = $(this).attr("pid").toString() ;
    var eml = this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id : id  
        },
        success:function(data){
            eml.innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
            document.getElementsByClassName('pro_amount').innerText = data.pro_amount
        }
    })
    
});


$(".remove-item").click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this
    console.log(id);
    console.log(eml);
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id : id  
        },
        success:function(data){
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
            document.getElementById('shippingcost').innerText = data.shippingcost
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })    
});