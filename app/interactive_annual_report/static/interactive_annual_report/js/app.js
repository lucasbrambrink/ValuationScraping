$(document).ready(function() {

    var apiBase = "/report/api/";
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
                var row = $('<a>')
                    .attr('href', '#' + items[ind])
                    .attr('id', 'ar-'+items[ind])
                    .append($('<span>').text(items[ind]))
                    .append("\t")
                    .append($('<span>').text(annualReport[items[ind]]));
                table.append(row);

                var className = '.' + items[ind];
                $(className).text( annualReport[items[ind]] );
            }
        return table;
    };

    var getKeyStatics = function( report_id ) {
        return $.get( apiBase + 'statics/' + report_id);
    };

    var generateFormula = function( keyStatics ) {
        for (var key in keyStatics) {
            var className = '.' + key;
            $(className).text( keyStatics[key] );
        }
    };



    /**
     *  Test
     *
     */

    $('#test-btn').on('click', function(e) {
        e.preventDefault();
        var res = getAnnualReport( 'IBM', '2013-12-31' );
        res.done(function( data ) {
                $('.stock').text(data.name + ' (' + data.symbol + ')');
                annualReport = data.annualReport[0];
                var table = generateAnnualTotal( annualReport );
                $('.annual-report').append( table );

                var res = getKeyStatics( annualReport.id );
                res.done(function( data ) {
                    var keyStatics = data.key_statics[0];
                    generateFormula( keyStatics );
        });
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

    $('.key-statics')
        .on('mouseover', '.factor', function() {
            var id = $(this).attr('class').split(' ')[1];
            $( '#' + id ).removeClass('hide');
            $( '#ar-' + id ).addClass('active');

        })
        .on('mouseout', '.factor', function() {
            var id = $(this).attr('class').split(' ')[1];
            $( '#' + id ).addClass('hide');
            $( '#ar-' + id ).removeClass('active');
    });


});
