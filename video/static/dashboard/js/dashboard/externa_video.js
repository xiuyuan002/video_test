
var videoEreaStatic=false;
var videoEdotArea=$('#video-edit-area')

$('#open-add-video-btn').click(function (){
    if(!videoEreaStatic){
        videoEdotArea.show();
        videoEreaStatic=true;
    }else{
        videoEdotArea.hide();
        videoEreaStatic=false;
    }
});