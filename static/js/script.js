$(document).ready(function () {
    $("#search_btn").click(function () {

        // taking input from frontend
        var year = $("#year_input").val();
        var make = $("#make_input").val();
        var model = $("#model_input").val();
        var mileage = $("#mileage_input").val();

        // error handeling for empty fields
        if(year == "" || make == "" || model == ""){
            return;
        }

        // disable search button while in search 

        $("#search_btn").prop("disabled", true);
        $("#search_btn").html(
            `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Searching...`
        );
        $("#result_section").addClass("hidden");

        $.get("search", { "year": year, "make": make, "model": model, "mileage": mileage }, function (data, status) {
            
            // popup if no data found
            
            if (!data["success"]) {
                alert(data["error"]);
                $("#search_btn").prop("disabled", false);
                $("#search_btn").html("Search");
                return;
            }

            $("#result_section").removeClass("hidden");

            $("#est_text").text("Estimation: $" + data["estimation"]);

            var tableData = "<thead><tr><th>Vehicle</th><th>Price</th><th>Mileage</th><th>Location</th></tr></thead><tbody>";
            
            // loop to insert vehicle data into table

            for (var i = 0; i < data["vehicles"].length; i++) {
                tableData += `<tr><td>${data["vehicles"][i]["year"]} ${data["vehicles"][i]["make"]} ${data["vehicles"][i]["model"]}</td>`
                tableData += `<td>${data["vehicles"][i]["price"]}</td>`
                tableData += `<td>${data["vehicles"][i]["mileage"]}</td>`
                tableData += `<td>${data["vehicles"][i]["dealer_street"]}</td></tr>`
            }

            tableData += "</tbody></table>";

            $("#table").html(tableData);

            $("#search_btn").prop("disabled", false);
            $("#search_btn").html("Search");
        });
    });
});