$(document).ready(function() {

    // Order the Columns
    $("th.sortable").click(function(){
        let table = $(this).parents('table').eq(0)
        let rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()))
        this.asc = !this.asc
        if (!this.asc){rows = rows.reverse()}
        for (let i = 0; i < rows.length; i++){table.append(rows[i])}
    })
    function comparer(index) {
        return function(a, b) {
            let valA = getCellValue(a, index), valB = getCellValue(b, index)
            return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.localeCompare(valB)
        }
    }
    function getCellValue(row, index){ return $(row).children('td').eq(index).text() }

    // Search functionality
    $("#searchInput").on("keyup", function() {
        let value = $(this).val().toLowerCase();
        $("#table tbody tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    // Check Box Columns Functionality
    let allCheckBox = $("#selectAll");
    let columnCheckBoxes = $(".form-check-input").not("#selectAll");

    allCheckBox.change(function() {
        columnCheckBoxes.prop('checked', this.checked).change();
    });

    columnCheckBoxes.change(function() {
        let columnClass = this.id;
        $("." + columnClass).toggle(this.checked);
        let allChecked = columnCheckBoxes.length === columnCheckBoxes.filter(":checked").length;
        allCheckBox.prop('checked', allChecked);
    });

    // Show the dropdown menu on hover
    $('.nav-item.dropdown').hover(function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeIn(200);
    }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeOut(200);
    });

    // Export Data as Excel Spread Sheet
    // Read CSRF token from meta tags
    let token = $("meta[name='_csrf']").attr("content");
    let header = $("meta[name='_csrf_header']").attr("content");

    // Set up AJAX to include the CSRF header
    $.ajaxSetup({
        beforeSend: function(xhr) {
            xhr.setRequestHeader(header, token);
        }
    });

    $('#exportBtn').off("click").on("click", function() {

        let tableArray = getSelectedOrAllRowsData();
        let filename = $('#exportBtn').data('filename')  + ".xlsx"; // Use default if empty or not set

        let payload = {
            tableData: tableArray,
            filename: filename + ".xlsx"
        };

        let jsonData = JSON.stringify(payload);
        let exportPath = $('#exportButtonPath').val();

        $.ajax({
            type: 'POST',
            url: exportPath,
            data: jsonData,
            contentType: 'application/json',
            dataType: 'binary',
            xhrFields: {
                responseType: 'blob'
            },
            success: function(response, status, xhr) {
                let blob = response;

                let link = document.createElement('a');
                link.href = window.URL.createObjectURL(blob);
                link.download = filename;
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            },
            error: function(xhr, status, error) {
                console.error('Export failed:', error);
            }
        });
    });

    // Print Current Page
    $("#printButton").off("click").on("click", function(event) {
        event.preventDefault();
        window.print();
    });

    $('#selectAllCheckbox').on('change', function() {
        $('.rowCheckbox').prop('checked', $(this).prop('checked'));
    });

    $('.rowCheckbox').on('change', function() {
        // Check if all checkboxes are selected
        if ($('.rowCheckbox:checked').length === $('.rowCheckbox').length) {
            $('#selectAllCheckbox').prop('checked', true);
        } else {
            $('#selectAllCheckbox').prop('checked', false);
        }
    });


});

function dismissMessage(alertId) {
    $('#' + alertId).fadeOut('slow', function() {
        console.log("dismissMessage called with:", alertId);
        $(this).remove();
    });
}

function getSelectedOrAllRowsData() {
    let tableArray = [];
    let selectedRows = $('#table tbody tr').has('td input[type="checkbox"]:checked');
    let rowsToProcess = selectedRows.length > 0 ? selectedRows : $('#table tbody tr');

    rowsToProcess.each(function() {
        let row = {};
        // Adjust index to skip checkbox column if needed
        $(this).find('td:not(:first-child)').each(function(index) {
            // Adjust index to align with header (skip checkbox header)
            let header = $('#table th').eq(index + 1).text().trim();
            row[header] = $(this).text().trim();
        });
        tableArray.push(row);
    });

    return tableArray;
}

function changePageSize() {
    $("#searchForm").submit();
}