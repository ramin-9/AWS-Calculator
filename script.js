async function calculate() {

    const num1 = document.getElementById("num1").value;
    const num2 = document.getElementById("num2").value;
    const operation = document.getElementById("operation").value;

    const response = await fetch("https://ugu84nr2bj.execute-api.ap-southeast-2.amazonaws.com/dev", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            num1: num1,
            num2: num2,
            operation: operation
        })

    });

    const data = await response.json();

    document.getElementById("result").innerText =
        "Result: " + data.result;

}