$(document).ready(function() {

    var apiBase = "/api/";
    var items = ['tr', 'gt', 'ebit', 'ie', 'ibt', 'ite', 'ni', 'cce', 'sti', 'inventory', 'tca', 'ppe', 'ta', 'tcl', 'ltd', 'mi', 'td', 'tl', 'ps', 'tse', 'tcso', 'sp', 'dp'];
    var annualReport = {};

    var getAnnualReport = function( symbol, year ) {

        return $.get( apiBase + 'get', {
            symbol: symbol,
            year: year
        })
    };

    var generateAnnualTotal = function( annualReport ) {
        var table = $('<pre>');
            for (var ind in items) {
                var row = $('<a>').attr('href', '#' + items[ind])
                    .append($('<span>').text(items[ind]))
                    .append("\t")
                    .append($('<span>').text(annualReport[items[ind]]));
                table.append(row);
            }
        return table;
    };




    /**
     *  Test
     *
     */

    $('#test-btn').on('click', function(e) {
        e.preventDefault();
        res = getAnnualReport( 'IBM', '2013-12-31' );
        res.done(function( data ) {
                $('.stock').text(data.name + ' (' + data.symbol + ')');
                annualReport = data.annualReport[0];
                var table = generateAnnualTotal( annualReport );
                $('.annual-report').append( table );
            });
    });

    $('.annual-report')
        .on('mouseover', 'a', function() {
        var explanationID = $(this).attr('href');
        $(explanationID).removeClass('hide');
    })
        .on('mouseout', 'a', function() {
        var explanationID = $(this).attr('href');
        $(explanationID).addClass('hide');
    });


});
