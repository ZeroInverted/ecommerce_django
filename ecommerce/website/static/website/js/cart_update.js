function main(){
    const csrftoken = document.cookie.split("=")[1];
    const cart_rows = document.querySelectorAll(".cart-row")
    let total_cart_sum = 0
    let total_quantity = 0
    cart_rows?.forEach( (cart_row) =>{
        cart_total = document.querySelector(".cart-total")
        const increase_btn = cart_row.querySelector(".up-change")
        const decrease_btn = cart_row.querySelector(".down-change")
        const quantity_paragraph = cart_row.querySelector("#quantity")
        const total_price_paragraph = cart_row.querySelector("#total-price")
        const total_items_paragraph = document.querySelector("#items-total")
        let quantity = parseInt(cart_row.getAttribute("data-quantity"))
        let unit_price = parseFloat(cart_row.getAttribute("data-price"))
        let total_price = 0
        if(!Number.isNaN(quantity)&& !Number.isNaN(unit_price)){
            total_price = quantity * unit_price
            console.log("q" + quantity)
            console.log("up" + unit_price)
            console.log("total price " + total_price)
            total_cart_sum += total_price
            total_quantity += quantity
        }

    
        
        increase_btn?.addEventListener("click", (e) =>{
            if(quantity != NaN){
                update_cart(quantity+1)
            }
        })
        
        decrease_btn?.addEventListener("click", (e)=>{
            if(quantity != NaN){
                update_cart(quantity-1)
            }
        })
    
        function update_cart(new_quantity){
            fetch("http://127.0.0.1:8000/cart", {
                method:"PUT",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({
                    pid:cart_row.getAttribute("data-pid"),
                    quantity:new_quantity
                })
            })
            .then((response) => {
                if (response.ok) {
                    // Update the displayed quantity
                        total_quantity -=quantity
                        quantity = new_quantity
                        total_quantity +=quantity
                        total_cart_sum -= total_price
                        total_price = quantity * unit_price
                        total_cart_sum += total_price
                        quantity_paragraph.textContent = `x${new_quantity}`;
                        cart_row.setAttribute("data-quantity", new_quantity);
                        total_items_paragraph.textContent = `${total_quantity}`
                        total_price_paragraph.textContent = `$${(total_price).toFixed(2)}`
                        cart_total.textContent = `$${(total_cart_sum).toFixed(2)}`
                }
            })
            .catch((error) => {
                console.error("Error updating cart:", error);
            });
        }
        
    });
}

main()