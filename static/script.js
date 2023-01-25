function deletePost(id) {
    var ajxReq = $.ajax( {
        url : '/posts/'+id,
        type : 'delete',
        data : '',
        success : function ( data ) {
            location.reload();
        },
        error : function ( jqXhr, textStatus, errorMessage ) {
            //alert("Erro:" + errorMessage);
            location.reload();

        }
    });
}

function deleteSubPost(id) {
    var ajxReq = $.ajax( {
        url : '/subposts/'+id,
        type : 'delete',
        data : '',
        success : function ( data ) {
            location.reload();
        },
        error : function ( jqXhr, textStatus, errorMessage ) {
            //alert("Erro:" + errorMessage);
            location.reload();

        }
    });
}