
function main(){

    const template =
    `   
        {{#each product }}
        <div class="col-lg-4 p-5 img-container">
        <img src="{{fields.img_url}}" alt="" class="thumbnail">
        <div class="box-element product">
          <h6><strong>{{fields.name_en}}</strong></h6>
          <hr>
    
          <button class="btn btn-outline-secondary add-btn"> Add To Cart</button>
          <a class="btn btn-outline-success" href="#">View</a>
          <h4 style="display: inline-block; float: right"><strong>$ {{fields.unit_price}}</strong></h4>
        </div>
    </div>
        {{/each}}
    `
    const csrftoken = document.cookie.split("=")[1];
    
    const filter_selector = document.querySelector("#filter-form")
    filter_selector?.addEventListener('submit', (e) => {
        e.preventDefault()
        const input_data = new FormData(e.target)
        const filter_category = input_data.get("category")
        const filter_price = input_data.get("price")
        const filter_pname = input_data.get("pname")
        fetch("http://127.0.0.1:8000/store", {
            method:"POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                category:filter_category,
                price:filter_price,
                pname:filter_pname
            })
        })
        .then(res => res.json())
        .then(res => {
            const products =JSON.parse(res)
            //builder is a function that requires the template to be compiled and returned to it, during compilation the {{variables}} are put into place.
            const builder = Handlebars.compile(template);
            //Mapping between the {{variables}} and the actual data returned by axios from the json file.
            const templateParamMapping = {product: products};
            //HTML is prepared after building and is passed to htmlResult
            const htmlResult = builder(templateParamMapping);
            const cardsContainer = document.querySelector("#products-container");
            //HTML result is appended in the html of the container.
            cardsContainer.innerHTML = htmlResult;
        })
    })
    const price_input=document.querySelector("#price")
    const price_span=document.querySelector("#price-span")
    price_input?.addEventListener("change", (e) => {
        price_span.innerText = "0 - " + e.target.value
    })

    const products = document.querySelectorAll(".product")
    products?.forEach( (product) =>{
        const btn = product.querySelector(".add-btn")
        btn?.addEventListener("click", (e)=>{
            fetch("http://127.0.0.1:8000/cart", {
                method:"POST",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({
                    pid:product.getAttribute("data-pid"),
                })
            })
        })
    })

    

    
}

main()