$(function(){

    var hasStart = false;
    var hasGet = true;
    var hasPost = false;

    $robo = new robot();

    var changeable = localStorage.getItem("hasChanged");
    function updateable(){
        changeable = localStorage.getItem("hasChanged");
    }
    setInterval(updateable, 1000);

    function updateGet(){
        if(!hasGet){
            //console.log("upgt: "+hasGet);
            if(changeable=="Y"){
                $.ajax({
                    type: 'GET',
                    dataType: 'json',
                    url: '/ChessApp/download_page/',
                    success: function(item){
                        var movemade = item.StateData.CompMadeMove;
                        var removemade = item.StateData.CompMadeRemove;
                        //console.log("comp moved: "+movemade);
                        if(movemade=="Y"&&removemade=="N"){ 
                            var statematrix2 = item.StateData.StateMatrix;
                            localStorage.setItem("StateMatrix", statematrix2);
                            var compchoice = item.StateData.CompChooses;
                            var compmove = item.StateData.CompMovesTo;
                            console.log("compchoice: "+compchoice+" compmove: "+compmove);
                            
                            $robo.select(compchoice);
                            $robo.moveTo(compmove);
                            hasGet = true;
                            //console.log("hasGet: "+hasGet);
                            console.log("get success");
                        }
                        else if(removemade=="Y"&&movemade=="Y"){ 
                            var statematrix2 = item.StateData.StateMatrix;
                            localStorage.setItem("StateMatrix", statematrix2);
                            var compchoice = item.StateData.CompChooses;
                            var compmove = item.StateData.CompMovesTo;
                            var compremove = item.StateData.CompRemoves;
                            console.log("compchoice: "+compchoice+" compmove: "+compmove+" compremove: "+compremove);
                            
                            $robo.select(compchoice);
                            $robo.remove(compremove);
                            $robo.moveTo(compmove);
                            hasGet = true;
                            //console.log("hasGet: "+hasGet);
                            console.log("get success");
                        }
                    },
                    error: function(){
                      console.log('get error');
                    }
                });
            }
        }
    }
    setInterval(updateGet, 1000);

    function updatePost(){
        if(!hasStart||hasGet){
            //console.log("uppt: "+hasGet);
            if(changeable=="Y"){
                var finmove = localStorage.getItem("FinishedMove");
                if(finmove=="Y"){
                    var statematrix1 = localStorage.getItem("StateMatrix");
                    var stmt = eval(statematrix1);
                    //console.log("state change: "+stmt[1][5].pieceId+" - "+stmt[3][5].pieceId)
                    $robo.kingMovement("bking");
                    var compcheck = localStorage.getItem("CompInCheck");
                    var compnwcheck = localStorage.getItem("CompNWInCheck");
                    var compnecheck = localStorage.getItem("CompNEInCheck");
                    var compswcheck = localStorage.getItem("CompSWInCheck");
                    var compsecheck = localStorage.getItem("CompSEInCheck");
                    var compupcheck = localStorage.getItem("CompUpInCheck");
                    var compdowncheck = localStorage.getItem("CompDownInCheck");
                    var comprightcheck = localStorage.getItem("CompRightInCheck");
                    var compleftcheck = localStorage.getItem("CompLeftInCheck");

                    var chkmt = localStorage.getItem("CheckMate");
                    var freemov = localStorage.getItem("FreeMove");
                    var curdir = localStorage.getItem("CurrentDirectionArray");
                    // console.log("curdir: "+curdir);
                    //curdir = eval(curdir);
                    var attckarr = localStorage.getItem("CurrentAttackerArray");
                    //attckarr = eval(attckarr);
                    var ingrd = localStorage.getItem("InGuard");
                    var pingrd = localStorage.getItem("PieceInGuard");
                    var spclngth = localStorage.getItem("FreeMovementLength");
                    var csk = localStorage.getItem("CanSaveKing");
                    var savers = localStorage.getItem("SaverArray");
                    var attck = localStorage.getItem("AttackerArray");
                    //console.log("puppet master: "+compnecheck);
                    var rmvdlist = localStorage.getItem("RemovedPiecesList");
                    var pwnidarr = localStorage.getItem("PawnIDArray");
                    var kmvd = localStorage.getItem("KingHasMoved");
                    var r1mvd = localStorage.getItem("Rook1HasMoved");
                    var r2mvd = localStorage.getItem("Rook2HasMoved");
                    // console.log("in puppetmaster - rook1HasMoved: "+r1mvd+" rook2HasMoved: "+r2mvd+" kingHasMoved: "+kmvd+" pawnIdArr: "+pwnidarr);
                    $.ajax({
                        type: 'POST',
                        url: '/ChessApp/create_page/',
                        dataType: 'json',
                        data: {
                            statemat: statematrix1,
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                            incheck: compcheck,
                            nwcheck: compnwcheck,
                            necheck: compnecheck,
                            swcheck: compswcheck,
                            secheck: compsecheck,
                            upcheck: compupcheck,
                            downcheck: compdowncheck,
                            rightcheck: comprightcheck,
                            leftcheck: compleftcheck,
                            checkmate: chkmt,
                            freemove: freemov,
                            currentdirarr: curdir,
                            attackerarray: attckarr,
                            inguard: ingrd,
                            pieceinguard: pingrd,
                            spacelength: spclngth,
                            cansaveking: csk,
                            savers: savers,
                            attackers: attck, 
                            pawnidarr: pwnidarr,
                            kingmvd: kmvd,
                            rook1mvd: r1mvd,
                            rook2mvd: r2mvd,
                            removedlist: rmvdlist,
                            section: 'StateMatrix'
                        },
                        success: function(item){
                            console.log("post success");
                            localStorage.setItem('FinishedMove', 'N');
                            hasGet = false;
                            hasStart = true;
                        },
                        error: function(){
                            console.log('post error');
                        }
                    });
                }
            }
        }
    }
    setInterval(updatePost, 1000);

});

