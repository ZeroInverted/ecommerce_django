function main(){

    const template =
    `   
        <tr>
            <th>Order ID</th>
            <th>Status</th>
        </tr>
        {{#each order }}
        <tr>
            <td>{{ pk }}</td> 
            <td>{{ fields.status }}</td>
        </tr>
        {{/each}}
    `
    const csrftoken = document.cookie.split("=")[1];
    console.log("" + csrftoken)
    
    
    const filter_selector = document.querySelector(".filter")
    filter_selector?.addEventListener('change', (e) => {
        const selected_option = e.target.value;
        fetch("http://127.0.0.1:8000/orders", {
            method:"POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                filter_field:selected_option
            })
        })
        .then(res => res.json())
        .then(res => {
            const orders =JSON.parse(res)
            //builder is a function that requires the template to be compiled and returned to it, during compilation the {{variables}} are put into place.
            const builder = Handlebars.compile(template);
            //Mapping between the {{variables}} and the actual data returned by axios from the json file.
            const templateParamMapping = {order: orders};
            //HTML is prepared after building and is passed to htmlResult
            const htmlResult = builder(templateParamMapping);
            const cardsContainer = document.querySelector(".order-table");
            //HTML result is appended in the html of the container.
            cardsContainer.innerHTML = htmlResult;
        })
    })
}

main()



