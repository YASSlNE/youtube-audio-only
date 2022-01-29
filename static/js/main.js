function hide_div(){
    $('#mp3').css('display','none');
    return true;
}
function get_links(){
    $('div#mp3').html($('#mp3').text()==''? '':$('#mp3').text());
    $('#mp3').css('display','block');
    return true;
}