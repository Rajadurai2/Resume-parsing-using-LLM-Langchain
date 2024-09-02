$(document).ready(function() {
    // Toggle the sidebar menu
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    // Handle form submission via AJAX
    $("#upload-form").on("submit", function(event) {
        event.preventDefault();

        var formData = new FormData(this);

        $.ajax({
            url: "/score",
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                // Update the result on the main page
                $("#score-result").text(`Your resume scored: ${response.score}% against the job description.`);
                //$("#score-result2").text(` ${response.user_details.name} `)
            
            error: function() {
                $("#score-result").text("An error occurred while scoring your resume. Please try again.");
            }

            }
        });
    });
});
