function robot(){
var boardMatrix = [
    ['r1A', 'r1B', 'r1C', 'r1D', 'r1E', 'r1F', 'r1G', 'r1H'],
    ['r2A', 'r2B', 'r2C', 'r2D', 'r2E', 'r2F', 'r2G', 'r2H'],
    ['r3A', 'r3B', 'r3C', 'r3D', 'r3E', 'r3F', 'r3G', 'r3H'],
    ['r4A', 'r4B', 'r4C', 'r4D', 'r4E', 'r4F', 'r4G', 'r4H'],
    ['r5A', 'r5B', 'r5C', 'r5D', 'r5E', 'r5F', 'r5G', 'r5H'],
    ['r6A', 'r6B', 'r6C', 'r6D', 'r6E', 'r6F', 'r6G', 'r6H'],
    ['r7A', 'r7B', 'r7C', 'r7D', 'r7E', 'r7F', 'r7G', 'r7H'],
    ['r8A', 'r8B', 'r8C', 'r8D', 'r8E', 'r8F', 'r8G', 'r8H'],
];

// var boardIdMatrix = [
//     [{ id : "", i : 0, j : 0 }, { id : "", i : 0, j : 1 }, { id : "", i : 0, j : 2 }, { id : "", i : 0, j : 3 }, 
//     { id : "", i : 0, j : 4 }, { id : "", i : 0, j : 5 }, { id : "", i : 0, j : 6 }, { id : "", i : 0, j : 7 }],
//     [{ id : "", i : 1, j : 0 }, { id : "", i : 1, j : 1 }, { id : "", i : 1, j : 2 }, { id : "", i : 1, j : 3 }, 
//     { id : "", i : 1, j : 4 }, { id : "", i : 1, j : 5 }, { id : "", i : 1, j : 6 }, { id : "", i : 1, j : 7 }],
//     [{ id : "", i : 2, j : 0 }, { id : "", i : 2, j : 1 }, { id : "", i : 2, j : 2 }, { id : "", i : 2, j : 3 }, 
//     { id : "", i : 2, j : 4 }, { id : "", i : 2, j : 5 }, { id : "", i : 2, j : 6 }, { id : "", i : 2, j : 7 }],
//     [{ id : "", i : 3, j : 0 }, { id : "", i : 3, j : 1 }, { id : "", i : 3, j : 2 }, { id : "", i : 3, j : 3 }, 
//     { id : "", i : 3, j : 4 }, { id : "", i : 3, j : 5 }, { id : "", i : 3, j : 6 }, { id : "", i : 3, j : 7 }],
//     [{ id : "", i : 4, j : 0 }, { id : "", i : 4, j : 1 }, { id : "", i : 4, j : 2 }, { id : "", i : 4, j : 3 }, 
//     { id : "", i : 4, j : 4 }, { id : "", i : 4, j : 5 }, { id : "", i : 4, j : 6 }, { id : "", i : 4, j : 7 }],
//     [{ id : "", i : 5, j : 0 }, { id : "", i : 5, j : 1 }, { id : "", i : 5, j : 2 }, { id : "", i : 5, j : 3 }, 
//     { id : "", i : 5, j : 4 }, { id : "", i : 5, j : 5 }, { id : "", i : 5, j : 6 }, { id : "", i : 5, j : 7 }], 
//     [{ id : "", i : 6, j : 0 }, { id : "", i : 6, j : 1 }, { id : "", i : 6, j : 2 }, { id : "", i : 6, j : 3 }, 
//     { id : "", i : 6, j : 4 }, { id : "", i : 6, j : 5 }, { id : "", i : 6, j : 6 }, { id : "", i : 6, j : 7 }],  
//     [{ id : "", i : 7, j : 0 }, { id : "", i : 7, j : 1 }, { id : "", i : 7, j : 2 }, { id : "", i : 7, j : 3 }, 
//     { id : "", i : 7, j : 4 }, { id : "", i : 7, j : 5 }, { id : "", i : 7, j : 6 }, { id : "", i : 7, j : 7 }],
// ]; 

var selected = undefined;
var I = 0;
var J = 0;
var placeId = '';
var type = '';
var left = 0;
var right = 0;
var up = 0;
var down = 0;
var pieces = document.getElementById('pieces');
var r = 0;
var l = 7;
var u = 7;
var d = 0;
//var uniqArr = [];

var conUniq = [];
var prev = '';
var firstVal = true;
var isPrev = undefined;

var nwleft = 0;
var nwup = 0;
var neright = 0;
var neup = 0;
var seright = 0;
var sedown = 0;
var swleft = 0;
var swdown = 0;

var nwArr = [];
var neArr = [];
var swArr = [];
var seArr = [];

var nw = undefined;
var ne = undefined;    
var sw = undefined;
var se = undefined;

var lefts = undefined;
var rights = undefined;
var ups = undefined;
var downs = undefined;

var pawntr = '';
var pawntl = '';
var pawntrch = undefined;
var pawntlch = undefined;
var isPawnFront = undefined;
var isPawnFront = undefined;
var fullArr = [];
var swtone = [];
var nwtose = [];
var currDir = [];

var kingsArray = [];
var horseArr = [];

var pawnIdArr = [];
var uniqPawn = undefined;

var isSelected = undefined;
var isMoved = undefined;
var isOpponent = undefined;

var nehorse = '';
var nwhorse = '';
var enhorse = '';
var wnhorse = '';
var eshorse = '';
var wshorse = '';
var sehorse = '';
var swhorse = '';

//console.log('HW path: '+window.location.href);

var pawntrEndNum = undefined;
var pawntlEndNum = undefined;
var pawnEndNum = undefined;

var colour = '';

var piecesFoundup = [];
var piecesFoundnw = [];
var piecesFoundne = [];
var piecesFoundright = [];
var piecesFoundleft = [];
var piecesFoundsw = [];
var piecesFoundse = [];
var piecesFounddown = [];

var highlights = [];

var castlerightArr1 = [];
var castlerightArr2 = [];
var castleleftArr1 = [];
var castleleftArr2 = [];
var kingHasMoved = false;
var rook1HasMoved = false;
var rook2HasMoved = false;
//var castleleftArr3 = [];

var piecesChecking = [];
var checkMate = false;
var kCheckMate = false;
var inCheck = false;
var isKing = false;


var leftId = '';
var rightId = '';
var upId = '';
var downId = '';

var nwId = '';
var neId = '';
var swId = '';
var seId = '';

var allIdArr = [];
var prevPawn = undefined; 
var checkArr = [];
var reachable = [];
var pawnHasMoved = false;

var latestVal = '';
var kingGuard = [];
var dirSec = '';
var isGuard = false;
var attackerArr = [];
var guardAttack = '';
var reached = false;
var freeMov = true;
var canSaveKing = false;
var kcanSaveKing = false;
var kingCanSaveKing = false;
var pcarr = [];
var pgarr = [];

var savers = [];
var attackers = [];

var setColour = 'blackPiece';
var oppColour = 'whitePiece';

var nestedPieceIds = [];

var livewire = new human(); 


this.select = function(controlId){
    //console.log("in check sel: "+inCheck);
    //console.log("selected");
    var newVal = localStorage.getItem('hasChanged');
    //console.log('in select: '+newVal);
    if(newVal == 'Y'){
    // console.log('robot selected: '+controlId);
    //console.log('select in check '+inCheck);
    selected = document.getElementById(controlId);
    type = selected.classList[1];
    colour = selected.classList[0];
    placeId = selected.parentNode.id;
    //console.log('placeId: '+placeId);
    var canSaveArr = [];
    place = document.getElementById(placeId);
    var freeAreas = [];
    isKing = false;
    pawntrEndNum = undefined;
    pawntlEndNum = undefined;
    pawnEndNum = undefined;
    horseArr = [];
    kingsArray = [];
    nwArr = [];
    neArr = [];
    swArr = [];
    seArr = [];
    pawnHasMoved = false;
    
    for(var i=0; i<8; i++){
        for(var j=0; j<8; j++){
            //console.log('has piece: '+square.firstChild);
            if(placeId==boardMatrix[i][j]){
                I = i;
                J = j;
                break;
            }
        }
    }  
    left = J;
    right = J;
    up = I;
    down = I;

    for(var g=0; g<highlights.length; g++){
        //console.log("h id: "+highlights[g]);
        highlights[g].style.background = 'initial';

    }

    if(type!='king'){
        //kingMovement('bking');
        kcanSaveKing = false;
        kingCanSaveKing = false;
    }
    
    
    if(inCheck||isGuard){
        freeMov = false;
    }else{
        freeMov = true;
    }



    //console.log("freeMov: "+freeMov);
    var nwleft = J;
    var nwup = I;
    var neright = J;
    var neup = I;
    var seright = J;
    var sedown = I;
    var swleft = J;
    var swdown = I;

    
    
      
     //initialises objects each time
    function movable(){
        // console.log("MOVEABLE");
        var rstart = false;
        var lstart = false;
        var ustart = false;
        var dstart = false;
        
        var nwstart = false;
        var nestart = false;
        var swstart = false;
        var sestart = false;

        var rArr = [];
        var lArr = [];
        var uArr = [];
        var dArr = [];

        for(var i=0; i<8; i++){
            // console.log("type: "+type+" is freemov: "+freeMov);
           if(type=='rook'&&freeMov||type=='queen'&&freeMov){
            //localStorage.setItem('hasSelected', 'N');
            //console.log('guard: '+isGuard+' check: '+inCheck);
            if(right>-1){
                //console.log('count right: '+right);
                rights = document.getElementById(boardMatrix[I][right]);
             
            }if(left<8){
                lefts = document.getElementById(boardMatrix[I][left]);
              
            }if(up>-1){
                ups = document.getElementById(boardMatrix[up][J]); 
               
                // console.log('place: '+boardMatrix[up][J]);
            }if(down<8){
                downs = document.getElementById(boardMatrix[down][J]);
                
                //console.log('movable: '+boardMatrix[down][J]);
            }
                    
               
           
            if(right<8&&right>-1){
                if(rights!=null){
                    if(!rights.firstElementChild||!rstart){
                        right--;

                        rstart = true;
                    }
                }
            }
            if(left>-1&&left<8){
                if(lefts!=null){
                    if(!lefts.firstElementChild||!lstart){
                        left++;
                        lstart = true;
                    }
                }
            }
            if(up<8&&up>-1){
                if(ups!=null){
                    if(!ups.firstElementChild||!ustart){
                        up--;
                        //console.log('hello up: '+up+' - '+ups);
                        ustart = true;
                    }
                }
            }
            if(down>-1&&down<8){
                if(downs!=null){
                    if(!downs.firstElementChild||!dstart){
                        down++;
                        dstart = true;
                    }
                }
            }
         
            if((right+1)<8&&(right+1)>-1){
                allIdArr.push(boardMatrix[I][right+1]);
            }if((left-1)<8&&(left-1)>-1){
                allIdArr.push(boardMatrix[I][left-1]);
            }if((up+1)<8&&(up+1)>-1){
                allIdArr.push(boardMatrix[up+1][J]);
            }if((down-1)<8&&(down-1)>-1){
                allIdArr.push(boardMatrix[down-1][J]); 
            }        
           
           }

           if(type=='rook'&&!freeMov||type=='queen'&&!freeMov){
            //localStorage.setItem('hasSelected', 'N');
            if(right>-1){

                var rgt = boardMatrix[I][right];
                //console.log('right: '+right+' - '+rgt);
                var rgts = document.getElementById(boardMatrix[I][right]);
                for(var q=0; q<currDir.length; q++){
                    if(rgt==currDir[q]){
                        rights = document.getElementById(boardMatrix[I][right]);
                      
                    }
                }
                for(var qa=0; qa<attackerArr.length; qa++){
                     if(rgt==attackerArr[qa]){
                        rights = document.getElementById(boardMatrix[I][right]);
                       
                     }
                }
                if(rgt==guardAttack&&isGuard){
                    rights = document.getElementById(boardMatrix[I][right]);
                   
                }
            }if(left<8){
                var lft = boardMatrix[I][left];
                var lfts = document.getElementById(boardMatrix[I][left]); 
                for(var r=0; r<currDir.length; r++){
                    if(lft==currDir[r]){
                        lefts = document.getElementById(boardMatrix[I][left]);
                       
                    }
                }
                for(var qa=0; qa<attackerArr.length; qa++){
                     if(lft==attackerArr[qa]){
                        lefts = document.getElementById(boardMatrix[I][left]);
                       
                     }
                 }
                if(lft==guardAttack&&isGuard){
                    lefts = document.getElementById(boardMatrix[I][left]);
                    
                }
            }if(up>-1){
                var upp = boardMatrix[up][J];
                var upps = document.getElementById(boardMatrix[up][J]); 
                for(var s=0; s<currDir.length; s++){
                    if(upp==currDir[s]){
                        ups = document.getElementById(boardMatrix[up][J]); 
                      
                    }
                }
                for(var qa=0; qa<attackerArr.length; qa++){
                     if(upp==attackerArr[qa]){
                        ups = document.getElementById(boardMatrix[up][J]); 
                    }
                 }
                if(upp==guardAttack&&isGuard){
                    ups = document.getElementById(boardMatrix[up][J]); 
                   
                }          
            }if(down<8){
                var dwn = boardMatrix[down][J];
                var dwns = document.getElementById(boardMatrix[down][J]);
                for(var t=0; t<currDir.length; t++){
                     if(dwn==currDir[t]){
                        downs = document.getElementById(boardMatrix[down][J]);
                      
                    }
                }
                 for(var qa=0; qa<attackerArr.length; qa++){
                     if(dwn==attackerArr[qa]){
                        downs = document.getElementById(boardMatrix[down][J]);
                       
                     }
                 }
                if(dwn==guardAttack&&isGuard){
                    downs = document.getElementById(boardMatrix[down][J]);
                    
                }
            }
                    
               
           
            if(right<8&&right>-1){
                if(rgts!=null){
                    if(!rgts.firstElementChild||!rstart){        
                        right--;
                        rstart = true;
                        //console.log('is guard count right: '+right);
                    }
                }
            }
            if(left>-1&&left<8){
                if(lfts!=null){
                    if(!lfts.firstElementChild||!lstart){       
                        left++;
                        lstart = true;
                    }
                }
            }
            if(up<8&&up>-1){
                if(upps!=null){
                    if(!upps.firstElementChild||!ustart){        
                        up--;
                        ustart = true;
                    }
                }
            }
            if(down>-1&&down<8){
                if(dwns!=null){
                    if(!dwns.firstElementChild||!dstart){           
                        down++;
                        dstart = true;
                    }
                }
            }
         

            if((right+1)<8&&(right+1)>-1){
                allIdArr.push(boardMatrix[I][right+1]);
            }if((left-1)<8&&(left-1)>-1){
                allIdArr.push(boardMatrix[I][left-1]);
            }if((up+1)<8&&(up+1)>-1){
                allIdArr.push(boardMatrix[up+1][J]);
            }if((down-1)<8&&(down-1)>-1){
                allIdArr.push(boardMatrix[down-1][J]); 
            }                
           
           }
        
            if(type=='bishop'&&freeMov||type=='queen'&&freeMov){
                //localStorage.setItem('hasSelected', 'N');
        
                if(nwleft<8&&nwup>-1){
                    nw = document.getElementById(boardMatrix[nwup][nwleft]);
                    nwArr.push(nw);
                   
                }if(neright>-1&&neup>-1){
                    ne = document.getElementById(boardMatrix[neup][neright]);
                    neArr.push(ne);
                    
                }if(swleft<8&&swdown<8){
                    sw = document.getElementById(boardMatrix[swdown][swleft]);
                    swArr.push(sw);
                }if(seright>-1&&sedown<8){
                    se = document.getElementById(boardMatrix[sedown][seright]);
                    seArr.push(se);
                  
                }         

                if(nwleft<8&&nwup>-1){
                    if(nw!=null){
                        if(!nw.firstElementChild||!nwstart){
                            nwleft++;
                            nwup--;
                            nwstart = true;
                        }     
                    }
                }
                if(neright>-1&&neup>-1){
                    if(ne!=null){
                        if(!ne.firstElementChild||!nestart){
                            neright--;
                            neup--;
                            nestart = true;
                        }
                    }
                }
                if(swleft<8&&swdown<8){
                    if(sw!=null){
                        if(!sw.firstElementChild||!swstart){
                            swleft++;
                            swdown++;
                            swstart = true;
                        }
                    }
                }
                if(seright>-1&&sedown<8){
                    if(se!=null){
                        if(!se.firstElementChild||!sestart){
                            seright--;
                            sedown++;
                            sestart = true;
                        } 
                    }
                }
                if((nwup+1)<8&&(nwleft-1)>-1&&(nwup+1)>-1&&(nwleft-1)<8&&!inCheck){
                    allIdArr.push(boardMatrix[nwup+1][nwleft-1]); 
                }
                if((neup+1)<8&&(neright+1)<8&&(neup+1)>-1&&(neright+1)>-1&&!inCheck){
                    allIdArr.push(boardMatrix[neup+1][neright+1]);
                }
                if((swdown-1)>-1&&(swleft-1)>-1&&(swdown-1)<8&&(swleft-1)<8&&!inCheck){
                    allIdArr.push(boardMatrix[swdown-1][swleft-1]);
                }
                if((sedown-1)>-1&&(seright+1)<8&&(sedown-1)<8&&(seright+1)>-1&&!inCheck){
                    allIdArr.push(boardMatrix[sedown-1][seright+1]);                 
                }
            }
             if(type=='bishop'&&!freeMov||type=='queen'&&!freeMov){
                //localStorage.setItem('hasSelected', 'N');
        
                if(nwleft<8&&nwup>-1){
                    var tl = boardMatrix[nwup][nwleft];
                    var tls = document.getElementById(boardMatrix[nwup][nwleft]);
                    for(var w=0; w<currDir.length; w++){
                        if(tl==currDir[w]){
                            nw = document.getElementById(boardMatrix[nwup][nwleft]);
                            nwArr.push(nw);
                           
                        }
                    }
                    for(var nn=0; nn<attackerArr.length; nn++){
                        if(tl==attackerArr[nn]){
                            nw = document.getElementById(boardMatrix[nwup][nwleft]);
                            nwArr.push(nw);
                           
                        }
                    }
                    if(tl==guardAttack&&isGuard){
                        nw = document.getElementById(boardMatrix[nwup][nwleft]);
                        nwArr.push(nw);
                        
                    }
                }if(neright>-1&&neup>-1){
                    var tr = boardMatrix[neup][neright];
                    var trs = document.getElementById(boardMatrix[neup][neright]);
                    for(var y=0; y<currDir.length; y++){
                        if(tr==currDir[y]){
                            ne = document.getElementById(boardMatrix[neup][neright]);
                            neArr.push(ne);
                            
                        }
                    }
                    for(var nn=0; nn<attackerArr.length; nn++){
                        if(tr==attackerArr[nn]){
                            ne = document.getElementById(boardMatrix[neup][neright]);
                            neArr.push(ne);
                            
                        }
                    }

                    if(tr==guardAttack&&isGuard){
                        ne = document.getElementById(boardMatrix[neup][neright]);
                        neArr.push(ne);
                        
                    }
                }if(swleft<8&&swdown<8){
                    var bl = boardMatrix[swdown][swleft];
                    var bls = document.getElementById(boardMatrix[swdown][swleft]); 
                    for(var z=0; z<currDir.length; z++){
                        if(bl==currDir[z]){
                            sw = document.getElementById(boardMatrix[swdown][swleft]);
                            swArr.push(sw);
                            
                        }
                    }
                    for(var nn=0; nn<attackerArr.length; nn++){
                        if(bl==attackerArr[nn]){
                            sw = document.getElementById(boardMatrix[swdown][swleft]);
                            swArr.push(sw);
                          
                        }
                    }
                    if(bl==guardAttack&&isGuard){
                        sw = document.getElementById(boardMatrix[swdown][swleft]);
                        swArr.push(sw);
                      
                    }
                }if(seright>-1&&sedown<8){
                    var br = boardMatrix[sedown][seright];
                    var brs = document.getElementById(boardMatrix[sedown][seright]);
                    for(var b=0; b<currDir.length; b++){
                        //console.log("se currDir: "+currDir[b]);
                        if(br==currDir[b]){
                            se = document.getElementById(boardMatrix[sedown][seright]);
                            seArr.push(se);
                           
                        }
                    }
                    for(var nn=0; nn<attackerArr.length; nn++){
                        if(br==attackerArr[nn]){
                            se = document.getElementById(boardMatrix[sedown][seright]);
                            seArr.push(se);
                            
                        }
                    }
                    if(br==guardAttack&&isGuard){
                        se = document.getElementById(boardMatrix[sedown][seright]);
                        seArr.push(se);
                      
                    }
                }         

                if(nwleft<8&&nwup>-1){
                    if(tls!=null){
                        if(!tls.firstElementChild||!nwstart){                
                            nwleft++;
                            nwup--;
                            nwstart = true;
                        }     
                    }
                }
                if(neright>-1&&neup>-1){
                    if(trs!=null){
                        if(!trs.firstElementChild||!nestart){                
                            neright--;
                            neup--;
                            nestart = true;
                        }
                    }
                }
                if(swleft<8&&swdown<8){
                    if(bls!=null){
                        if(!bls.firstElementChildd||!swstart){               
                            swleft++;
                            swdown++;
                            swstart = true;
                        }
                    }
                }
                if(seright>-1&&sedown<8){
                    if(brs!=null){
                        if(!brs.firstElementChild||!sestart){
                            seright--;
                            sedown++;
                            sestart = true;
                        } 
                    }
                }
                if((nwup+1)<8&&(nwleft-1)>-1&&(nwup+1)>-1&&(nwleft-1)<8&&!inCheck){
                    allIdArr.push(boardMatrix[nwup+1][nwleft-1]); 
                }
                if((neup+1)<8&&(neright+1)<8&&(neup+1)>-1&&(neright+1)>-1&&!inCheck){
                    allIdArr.push(boardMatrix[neup+1][neright+1]);
                }
                if((swdown-1)>-1&&(swleft-1)>-1&&(swdown-1)<8&&(swleft-1)<8&&!inCheck){
                    allIdArr.push(boardMatrix[swdown-1][swleft-1]);
                }
                if((sedown-1)>-1&&(seright+1)<8&&(sedown-1)<8&&(seright+1)>-1&&!inCheck){
                    allIdArr.push(boardMatrix[sedown-1][seright+1]);                 
                }
               
            }          
        }     
    }  
    movable();
     
    if(type=='pawn'&&freeMov){
        //console.log("helo pawn");
        //localStorage.setItem('hasSelected', 'N');
        var m = 0;
        if(firstVal){
            firstVal = false;
            uniqPawn = true;
            //console.log('hello first val');
        }
        else if(!firstVal){
            //console.log('hello ununique')
            for(m=0; m<pawnIdArr.length; m++){
                if(controlId==pawnIdArr[m]){
                    //console.log('non unique');
                    uniqPawn = false;
                    break;
                }
            }

            if(m==pawnIdArr.length){
                uniqPawn = true;
            }
    
        }
        if(I-1>-1&&J-1>-1){
            var pawntrval = document.getElementById(boardMatrix[I-1][J-1]);
            pawntrEndNum = J-1;
            if(pawntrval.hasChildNodes()){
                var pawntrchild = pawntrval.firstElementChild;
                var theCol = pawntrchild.classList[0];
                if(theCol!=colour){
                    pawntr = boardMatrix[I-1][J-1];
                    allIdArr.push(boardMatrix[I-1][J-1]);
                }
            }
        }
        if(I-1>-1&&J+1<8){
            var pawntlval = document.getElementById(boardMatrix[I-1][J+1]);
            pawntlEndNum = J+1;
            if(pawntlval.hasChildNodes()){
                var pawntlchild = pawntlval.firstElementChild;
                var theCol = pawntlchild.classList[0];
                //console.log('theCol: '+theCol+' colour: '+colour);
                if(theCol!=colour){
                    pawntl = boardMatrix[I-1][J+1];
                    allIdArr.push(boardMatrix[I-1][J+1]);
                }
            }         
        }
        if(I-1>-1){
            var pawnFront = document.getElementById(boardMatrix[I-1][J]);
            pawnEndNum = J;  
            if(!pawnFront.hasChildNodes()){
                isPawnFront = false;
                allIdArr.push(boardMatrix[I-1][J]);
            }if(pawnFront.hasChildNodes()){
                isPawnFront = true;
            }
        }
        if(I-2>-1){
            var pawnFront2 = document.getElementById(boardMatrix[I-2][J]);
            pawnEndNum = J; 
            if(!pawnFront2.hasChildNodes()&&uniqPawn){
                isPawnFront2 = false;
                allIdArr.push(boardMatrix[I-2][J]);                    
            }if(pawnFront2.hasChildNodes()){
                isPawnFront2 = true;
            }
        } 
    }  
    
    if(type=='pawn'&&!freeMov){
        //localStorage.setItem('hasSelected', 'N');
        //console.log('is guard: '+isGuard);
        var m = 0;
        if(firstVal){
            pawnIdArr.push(controlId);
            firstVal = false;
            uniqPawn = true;
        }
        else if(!firstVal){
            //console.log('hello ununique')
            for(m=0; m<pawnIdArr.length; m++){
                if(controlId==pawnIdArr[m]){
                    uniqPawn = false;
                    break;
                }            
            }

            if(m==pawnIdArr.length){
                pawnIdArr.push(controlId);
                uniqPawn = true;
            }
    
        }
    
    
        if(I-1>-1&&J-1>-1){
            var pawntrval = document.getElementById(boardMatrix[I-1][J-1]);
            var pwntrpos = boardMatrix[I-1][J-1];
            pawntrEndNum = J-1;
            //if in check attacker or if isguard guardattack
            for(var nn=0; nn<attackerArr.length; nn++){
                if(pwntrpos==attackerArr[nn]){
                    if(pawntrval.hasChildNodes()){
                        var pawntrchild = pawntrval.firstElementChild;
                        var theCol = pawntrchild.classList[0];
                        if(theCol!=colour){
                            pawntr = boardMatrix[I-1][J-1];
                            allIdArr.push(boardMatrix[I-1][J-1]);
                        }
                    }
                }
            }
            for(var nn=0; nn<currDir.length; nn++){
                if(pwntrpos==currDir[nn]){
                    if(pawntrval.hasChildNodes()){
                        var pawntrchild = pawntrval.firstElementChild;
                        var theCol = pawntrchild.classList[0];
                        if(theCol!=colour){
                            pawntr = boardMatrix[I-1][J-1];
                            allIdArr.push(boardMatrix[I-1][J-1]);
                        }
                    }
                }
            }
            if(pwntrpos==guardAttack){
                if(pawntrval.hasChildNodes()){
                    var pawntrchild = pawntrval.firstElementChild;
                    var theCol = pawntrchild.classList[0];
                    if(theCol!=colour){
                        pawntr = boardMatrix[I-1][J-1];
                        allIdArr.push(boardMatrix[I-1][J-1]);
                    }
                }
            }
        }
        if(I-1>-1&&J+1<8){
            var pawntlval = document.getElementById(boardMatrix[I-1][J+1]);
            var pwntlpos = boardMatrix[I-1][J+1];
            pawntlEndNum = J+1;
            for(var nn=0; nn<attackerArr.length; nn++){
                if(pwntlpos==attackerArr[nn]){
                    if(pawntlval.hasChildNodes()){
                        var pawntlchild = pawntlval.firstElementChild;
                        var theCol = pawntlchild.classList[0];
                        //console.log('theCol: '+theCol+' colour: '+colour);
                        if(theCol!=colour){
                            pawntl = boardMatrix[I-1][J+1];
                            allIdArr.push(boardMatrix[I-1][J+1]);
                        }
                    }    
                }
            }
            for(var nn=0; nn<currDir.length; nn++){
                if(pwntlpos==currDir[nn]){
                    if(pawntlval.hasChildNodes()){
                        var pawntlchild = pawntlval.firstElementChild;
                        var theCol = pawntlchild.classList[0];
                        if(theCol!=colour){
                            pawntl = boardMatrix[I-1][J+1];
                            allIdArr.push(boardMatrix[I-1][J+1]);
                        }
                    }    
                }
            }
            if(pwntlpos==guardAttack){
                if(pawntlval.hasChildNodes()){
                    var pawntlchild = pawntlval.firstElementChild;
                    var theCol = pawntlchild.classList[0];
                    if(theCol!=colour){
                        pawntl = boardMatrix[I-1][J+1];
                        allIdArr.push(boardMatrix[I-1][J+1]);
                    }
                }     
            }    
        }
    
    

        //console.log('pawntr: '+pawntrch+' pawntl: '+pawntlch);
        if(I-1>-1){
            var pawnFront = document.getElementById(boardMatrix[I-1][J]);
            var pwnfrpos = boardMatrix[I-1][J];
            pawnEndNum = J;
            for(var c=0; c<currDir.length; c++){
                if(pwnfrpos==currDir[c]){   
                    if(!pawnFront.hasChildNodes()){
                        isPawnFront = false;
                        allIdArr.push(boardMatrix[I-1][J]);
                    }if(pawnFront.hasChildNodes()){
                        isPawnFront = true;
                    }
                }
            }
            for(var c=0; c<attackerArr.length; c++){
                if(pwnfrpos==attackerArr[c]){   
                    if(!pawnFront.hasChildNodes()){
                        isPawnFront = false;
                        allIdArr.push(boardMatrix[I-1][J]);
                    }if(pawnFront.hasChildNodes()){
                        isPawnFront = true;
                    }
                }
            }
            if(pwnfrpos==guardAttack){
                if(!pawnFront.hasChildNodes()){
                    isPawnFront = false;
                    allIdArr.push(boardMatrix[I-1][J]);
                }if(pawnFront.hasChildNodes()){
                    isPawnFront = true;
                }
            }
        }
        if(I-2>-1){
            var pawnFront2 = document.getElementById(boardMatrix[I-2][J]);
            var pwnfr2pos = boardMatrix[I-2][J];
            pawnEndNum = J;
            for(var d=0; d<currDir.length; d++){
                if(pwnfr2pos==currDir[d]){
                    if(!pawnFront2.hasChildNodes()&&uniqPawn){
                        isPawnFront2 = false;
                        allIdArr.push(boardMatrix[I-2][J]);
                    }if(pawnFront2.hasChildNodes()){
                        isPawnFront2 = true;
                    }
                } 
            } 
            for(var d=0; d<attackerArr.length; d++){
                if(pwnfr2pos==attackerArr[d]){
                    if(!pawnFront2.hasChildNodes()&&uniqPawn){
                        isPawnFront2 = false;
                        allIdArr.push(boardMatrix[I-2][J]);
                    }if(pawnFront2.hasChildNodes()){
                        isPawnFront2 = true;
                    }
                } 
            } 
            if(pwnfr2pos==guardAttack){
                if(!pawnFront2.hasChildNodes()&&uniqPawn){
                    isPawnFront2 = false;
                    allIdArr.push(boardMatrix[I-2][J]);
                }if(pawnFront2.hasChildNodes()){
                    isPawnFront2 = true;
                }
            }  
        }
    }
    

    fullArr = nwArr.concat(neArr).concat(swArr).concat(seArr);

    swtone = swArr.concat(neArr);
    nwtose = nwArr.concat(seArr);

    
    //console.log('horseArr '+horseArr);
    if(type=='horse'&&freeMov){
        //localStorage.setItem('hasSelected', 'N');
        if([I+2]<8&&[J-1]>-1){
            horseArr.push(boardMatrix[I+2][J-1]);
            allIdArr.push(boardMatrix[I+2][J-1]);
        }
        if([I+2]<8&&[J+1]<8){
            horseArr.push(boardMatrix[I+2][J+1]);
            allIdArr.push(boardMatrix[I+2][J+1]);
        }
        if([I+1]<8&&[J+2]<8){
            //console.log('j+2 i+1');
            horseArr.push(boardMatrix[I+1][J+2]);
            allIdArr.push(boardMatrix[I+1][J+2]);
        }
        if([I-1]>-1&&[J+2]<8){
            horseArr.push(boardMatrix[I-1][J+2]);
            allIdArr.push(boardMatrix[I-1][J+2]);
        }
        if([I-2]>-1&&[J+1]<8){
            horseArr.push(boardMatrix[I-2][J+1]);
            allIdArr.push(boardMatrix[I-2][J+1]);
        }
        if([I-2]>-1&&[J-1]>-1){
            horseArr.push(boardMatrix[I-2][J-1]);
            allIdArr.push(boardMatrix[I-2][J-1]);
        }
        if([I+1]<8&&[J-2]>-1){
            horseArr.push(boardMatrix[I+1][J-2]);
            allIdArr.push(boardMatrix[I+1][J-2]);
        }
        if([I-1]>-1&&[J-2]>-1){
            horseArr.push(boardMatrix[I-1][J-2]);
            allIdArr.push(boardMatrix[I-1][J-2]);
        }
        //console.log('in horse arr: '+horseArr);
    }
    if(type=='horse'&&!freeMov){
        //localStorage.setItem('hasSelected', 'N');
        if([I+2]<8&&[J-1]>-1){
            for(var ha=0; ha<currDir.length; ha++){
                if(currDir[ha]==boardMatrix[I+2][J-1]){
                    horseArr.push(boardMatrix[I+2][J-1]);
                    allIdArr.push(boardMatrix[I+2][J-1]);
                }
            }
           for(var ha=0; ha<attackerArr.length; ha++){
                if(attackerArr[ha]==boardMatrix[I+2][J-1]){
                    horseArr.push(boardMatrix[I+2][J-1]);
                    allIdArr.push(boardMatrix[I+2][J-1]);
                }
            }
            if(boardMatrix[I+2][J-1]==guardAttack){
                horseArr.push(boardMatrix[I+2][J-1]);
                allIdArr.push(boardMatrix[I+2][J-1]);
            }
        }
        if([I+2]<8&&[J+1]<8){
            for(var hb=0; hb<currDir.length; hb++){
                if(currDir[hb]==boardMatrix[I+2][J+1]){
                    horseArr.push(boardMatrix[I+2][J+1]);
                }
            }
          for(var hb=0; hb<attackerArr.length; hb++){
                if(attackerArr[hb]==boardMatrix[I+2][J+1]){
                    horseArr.push(boardMatrix[I+2][J+1]);
                    allIdArr.push(boardMatrix[I+2][J+1]);
                }
            }
            if(boardMatrix[I+2][J+1]==guardAttack){
                horseArr.push(boardMatrix[I+2][J+1]);
                allIdArr.push(boardMatrix[I+2][J+1]);;
            }
        }
        if([I+1]<8&&[J+2]<8){
            for(var hc=0; hc<currDir.length; hc++){
                if(currDir[hc]==boardMatrix[I+1][J+2]){
                    horseArr.push(boardMatrix[I+1][J+2]);
                    allIdArr.push(boardMatrix[I+1][J+2]);
                }
            }
            for(var hc=0; hc<attackerArr.length; hc++){
                if(attackerArr[hc]==boardMatrix[I+1][J+2]){
                    horseArr.push(boardMatrix[I+1][J+2]);
                    allIdArr.push(boardMatrix[I+1][J+2]);
                }
            }
            if(boardMatrix[I+1][J+2]==guardAttack){
                horseArr.push(boardMatrix[I+1][J+2]);
                allIdArr.push(boardMatrix[I+1][J+2]);
            }
        }
        if([I-1]>-1&&[J+2]<8){
            for(var hd=0; hd<currDir.length; hd++){
                if(currDir[hd]==boardMatrix[I-1][J+2]){
                    horseArr.push(boardMatrix[I-1][J+2]);
                    allIdArr.push(boardMatrix[I-1][J+2]);
                }
            }
            for(var hd=0; hd<attackerArr.length; hd++){
                if(attackerArr[hd]==boardMatrix[I-1][J+2]){
                    horseArr.push(boardMatrix[I-1][J+2]);
                    allIdArr.push(boardMatrix[I-1][J+2]);
                }
            }
            if(boardMatrix[I-1][J+2]==guardAttack){
                horseArr.push(boardMatrix[I-1][J+2]);
                allIdArr.push(boardMatrix[I-1][J+2]);
            }
        }
        if([I-2]>-1&&[J+1]<8){
             for(var he=0; he<currDir.length; he++){
                if(currDir[he]==boardMatrix[I-2][J+1]){
                    horseArr.push(boardMatrix[I-2][J+1]);
                    allIdArr.push(boardMatrix[I-2][J+1]);
                }
            }
            for(var he=0; he<attackerArr.length; he++){
                if(attackerArr[he]==boardMatrix[I-2][J+1]){
                    horseArr.push(boardMatrix[I-2][J+1]);
                    allIdArr.push(boardMatrix[I-2][J+1]);
                }
            }
            if(boardMatrix[I-2][J+1]==guardAttack){
                horseArr.push(boardMatrix[I-2][J+1]);
                allIdArr.push(boardMatrix[I-2][J+1]);
            }
        }
        if([I-2]>-1&&[J-1]>-1){
            for(var hf=0; hf<currDir.length; hf++){
                if(currDir[hf]==boardMatrix[I-2][J-1]){
                    horseArr.push(boardMatrix[I-2][J-1]);
                    allIdArr.push(boardMatrix[I-2][J-1]);
                }
            }
            for(var hf=0; hf<attackerArr.length; hf++){
                if(attackerArr[hf]==boardMatrix[I-2][J-1]){
                    horseArr.push(boardMatrix[I-2][J-1]);
                    allIdArr.push(boardMatrix[I-2][J-1]);
                }
            }
            if(boardMatrix[I-2][J-1]==guardAttack){
                horseArr.push(boardMatrix[I-2][J-1]);
                allIdArr.push(boardMatrix[I-2][J-1]);
            }
        }
        if([I+1]<8&&[J-2]>-1){
            for(var hg=0; hg<currDir.length; hg++){
                if(currDir[hg]==boardMatrix[I+1][J-2]){
                    horseArr.push(boardMatrix[I+1][J-2]);
                    allIdArr.push(boardMatrix[I+1][J-2]);
                }
            }
            for(var hg=0; hg<attackerArr.length; hg++){
                if(attackerArr[hg]==boardMatrix[I+1][J-2]){
                    horseArr.push(boardMatrix[I+1][J-2]);
                    allIdArr.push(boardMatrix[I+1][J-2]);
                }
            }
            if(boardMatrix[I+1][J-2]==guardAttack){
                horseArr.push(boardMatrix[I+1][J-2]);
                allIdArr.push(boardMatrix[I+1][J-2]);  
            }
        }
        if([I-1]>-1&&[J-2]>-1){
            for(var hh=0; hh<currDir.length; hh++){
                if(currDir[hh]==boardMatrix[I-1][J-2]){
                    horseArr.push(boardMatrix[I-1][J-2]);
                    allIdArr.push(boardMatrix[I-1][J-2]);
                }
            }
            for(var hh=0; hh<attackerArr.length; hh++){
                if(attackerArr[hh]==boardMatrix[I-1][J-2]){
                    horseArr.push(boardMatrix[I-1][J-2]);
                    allIdArr.push(boardMatrix[I-1][J-2]);
                }
            }
            if(boardMatrix[I-1][J-2]==guardAttack){
                horseArr.push(boardMatrix[I-1][J-2]);
                allIdArr.push(boardMatrix[I-1][J-2]);
            }
        }
        //console.log('in horse arr: '+horseArr);
    }
    
    if(type=='king'){ 
        //localStorage.setItem('hasSelected', 'N');
        //console.log('hello king: ');
        freeAreas = [];
        if([I+1]<8&&[J-1]>-1){
            var nwCheck = false;
            var val = document.getElementById(boardMatrix[I+1][J-1]);
            my_piece = null;
            my_piece_colour = ''; 
            if(val.hasChildNodes()){
                my_piece = val.firstElementChild;
                my_piece_colour = my_piece.classList[0];
            }
            var pieceArr = isChecked(boardMatrix[I+1][J-1], piecesFoundnw);
            for(var b=0; b<pieceArr.length; b++){
                nwCheck = canCheck(pieceArr[b], boardMatrix[I+1][J-1]);
                //console.log('nw check: '+b+' - '+pieceArr[b]);

                if(nwCheck){
                    break;
                }
            }

            if(nwCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[I+1][J-1]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!nwCheck&&!val.hasChildNodes()||my_piece&&my_piece_colour!=colour){
                //console.log('nw check');
                kingsArray.push(boardMatrix[I+1][J-1]);  
                allIdArr.push(boardMatrix[I+1][J-1]);
                freeAreas.push(boardMatrix[I+1][J-1]); 
            }
        }
        if([I+1]<8){
            var upCheck = false;
            var pieceArr = isChecked(boardMatrix[I+1][J], piecesFoundup);
            //console.log('wats up dude');
            var val = document.getElementById(boardMatrix[I+1][J]);
            my_piece = null;
            my_piece_colour = ''; 
            if(val.hasChildNodes()){
                my_piece = val.firstElementChild;
                my_piece_colour = my_piece.classList[0];
            }
            for(var b=0; b<pieceArr.length; b++){
                upCheck = canCheck(pieceArr[b], boardMatrix[I+1][J]);
                //console.log('up check: '+b+' - '+pieceArr[b]+' - '+upCheck);
                if(upCheck){
                    break;
                }
            }
            if(upCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[I+1][J]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!upCheck&&!val.hasChildNodes()||my_piece&&my_piece_colour!=colour){
                kingsArray.push(boardMatrix[I+1][J]); 
                allIdArr.push(boardMatrix[I+1][J]);
                freeAreas.push(boardMatrix[I+1][J]);  
            }
            
        }    
        if([I+1]<8&&[J+1]<8){
            var neCheck = false;
            var pieceArr = isChecked(boardMatrix[I+1][J+1], piecesFoundne);
            var val = document.getElementById(boardMatrix[I+1][J+1]);
            my_piece = null;
            my_piece_colour = ''; 
            if(val.hasChildNodes()){
                my_piece = val.firstElementChild;
                my_piece_colour = my_piece.classList[0];
            }
            for(var b=0; b<pieceArr.length; b++){
                neCheck = canCheck(pieceArr[b], boardMatrix[I+1][J+1]);
                //console.log('ne check: '+b+' - '+pieceArr[b]);
                if(neCheck){
                    break;
                }
                //console.log('is checked: '+pieceArr[b]+' - '+neCheck);
            }
            if(neCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[I+1][J+1]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!neCheck&&!val.hasChildNodes()||my_piece&&my_piece_colour!=colour){
                kingsArray.push(boardMatrix[I+1][J+1]);
                allIdArr.push(boardMatrix[I+1][J+1]);
                freeAreas.push(boardMatrix[I+1][J+1]);
            }
            
        }
        if([J-1]>-1){
            var leftCheck = false;
            var pieceArr = isChecked(boardMatrix[I][J-1], piecesFoundleft);
            var val = document.getElementById(boardMatrix[I][J-1]);
            my_piece = null;
            my_piece_colour = ''; 
            if(val.hasChildNodes()){
                my_piece = val.firstElementChild;
                my_piece_colour = my_piece.classList[0];
            }
            for(var b=0; b<pieceArr.length; b++){
                leftCheck = canCheck(pieceArr[b], boardMatrix[I][J-1]);
                //console.log('left check: '+b+' - '+pieceArr[b]);
                if(leftCheck){
                    break;
                }
                //console.log('is checked: '+b+' '+leftCheck);
            }
            //console.log('left check');
            if(leftCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[I][J-1]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!leftCheck&&!val.hasChildNodes()||my_piece&&my_piece_colour!=colour){
                kingsArray.push(boardMatrix[I][J-1]);
                allIdArr.push(boardMatrix[I][J-1]);
                freeAreas.push(boardMatrix[I][J-1]);   
            }
            
        }
        if([J+1]<8){
            var rightCheck = false;
            var pieceArr = isChecked(boardMatrix[I][J+1], piecesFoundright);
            var val = document.getElementById(boardMatrix[I][J+1]);
            my_piece = null;
            my_piece_colour = ''; 
            if(val.hasChildNodes()){
                my_piece = val.firstElementChild;
                my_piece_colour = my_piece.classList[0];
            }
            for(var b=0; b<pieceArr.length; b++){
                rightCheck = canCheck(pieceArr[b], boardMatrix[I][J+1]);
                //console.log('right check: '+b+' - '+pieceArr[b]);
                if(rightCheck){
                    break;
                }
                //console.log('is checked: '+b+' '+rightCheck);
            }
            //console.log('right check');
            if(rightCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[I][J+1]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!rightCheck&&!val.hasChildNodes()||my_piece&&my_piece_colour!=colour){
                kingsArray.push(boardMatrix[I][J+1]);
                allIdArr.push(boardMatrix[I][J+1]);
                freeAreas.push(boardMatrix[I][J+1]);
            }
            
        }
        if([I-1]>-1&&[J-1]>-1){
            var swCheck = false;
            var pieceArr = isChecked(boardMatrix[I-1][J-1], piecesFoundsw);
            var val = document.getElementById(boardMatrix[I-1][J-1]);
            my_piece = null;
            my_piece_colour = ''; 
            if(val.hasChildNodes()){
                my_piece = val.firstElementChild;
                my_piece_colour = my_piece.classList[0];
            }
            for(var b=0; b<pieceArr.length; b++){
                swCheck = canCheck(pieceArr[b], boardMatrix[I-1][J-1]);
                //console.log('sw check: '+b+' - '+pieceArr[b]);
                if(swCheck){
                    break;
                }
                //console.log('is checked: '+b+' '+swCheck);
            }
            if(swCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[I-1][J-1]);
                val.style.background = 'orange'; 
                highlights.push(val);
            }else if(!swCheck&&!val.hasChildNodes()||my_piece&&my_piece_colour!=colour){
                kingsArray.push(boardMatrix[I-1][J-1]);
                allIdArr.push(boardMatrix[I-1][J-1]);
                freeAreas.push(boardMatrix[I-1][J-1]);  
            }
            
        }
        if([I-1]>-1){
            var downCheck = false;
            var pieceArr = isChecked(boardMatrix[I-1][J], piecesFounddown);
            var val = document.getElementById(boardMatrix[I-1][J]);
            my_piece = null;
            my_piece_colour = ''; 
            if(val.hasChildNodes()){
                my_piece = val.firstElementChild;
                my_piece_colour = my_piece.classList[0];
            }
            for(var b=0; b<pieceArr.length; b++){
                downCheck = canCheck(pieceArr[b], boardMatrix[I-1][J]);
                //console.log('down check: '+b+' - '+pieceArr[b]);
                 if(downCheck){
                    break;
                }
                //console.log('is checked: '+b+' '+downCheck);
            }
            if(downCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[I-1][J]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!downCheck&&!val.hasChildNodes()||my_piece&&my_piece_colour!=colour){
                kingsArray.push(boardMatrix[I-1][J]);
                allIdArr.push(boardMatrix[I-1][J]);
                freeAreas.push(boardMatrix[I-1][J]);    
            }
            
        }
        if([I-1]>-1&&[J+1]<8){
            var seCheck = false;
            var pieceArr = isChecked(boardMatrix[I-1][J+1], piecesFoundse);
            var val = document.getElementById(boardMatrix[I-1][J+1]);
            my_piece = null;
            my_piece_colour = ''; 
            if(val.hasChildNodes()){
                my_piece = val.firstElementChild;
                my_piece_colour = my_piece.classList[0];
            }
            for(var b=0; b<pieceArr.length; b++){
                seCheck = canCheck(pieceArr[b], boardMatrix[I-1][J+1]);
                //console.log('se check: '+b+' - '+pieceArr[b]);
                if(seCheck){
                    break;
                }
                //console.log('is checked: '+b+' '+seCheck);
            }
            if(seCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[I-1][J+1]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!seCheck&&!val.hasChildNodes()||my_piece&&my_piece_colour!=colour){
                kingsArray.push(boardMatrix[I-1][J+1]);
                allIdArr.push(boardMatrix[I-1][J+1]);
                freeAreas.push(boardMatrix[I-1][J+1]);  
            }
            
        }
            // //console.log('in check: '+inCheck);
            // var canReach = false;
            // inCheck = false;
            // isGuard = false;
            // checkArr = [];
            // var pieceAr = kingIsChecked(boardMatrix[I][J], piecesChecking);
            // checkArr = pieceAr;
            // var val = document.getElementById(boardMatrix[I][J]);
            // for(var b=0; b<pieceAr.length; b++){
            //     canReach = kingCanCheck(pieceAr[b], boardMatrix[I][J]);
            //     if(canReach){
            //         reachable.push(pieceAr[b]);
            //     }
            // }
            // var a = undefined;
            // //console.log("reachable: "+reachable);
            // for(var r=0; r<reachable.length; r++){
            //     var tempAt = document.getElementById(reachable[r]);
            //     var nextAt = tempAt.parentNode.id;
            //     attackerArr.push(nextAt);
            //     inCheck = finalCanCheck(reachable[r], boardMatrix[I][J]);
            //     //console.log("curr: "+currDir);
            //     if(inCheck){
            //         canSaveKing =  trySave();
            //         var tempcansave =  tryGet(I, J);
            //         if(!canSaveKing){
            //             canSaveKing = tempcansave;
            //         }           
            //         break;
            //     }
            // }
            // //console.log('king In check: '+inCheck);
            // if(inCheck){
            //     val = document.getElementById(boardMatrix[I][J]);
            //     //console.log("freeareas: "+kfreeAreas.length==0);
            //     if(freeAreas.length==0&&!canSaveKing){
            //         CheckMate = true;
            //         //console.log("hello checkmate");
            //     }else{
            //         CheckMate = false;
            //     }
            //     dispChckMt = document.getElementById("checkmate");
            //     if(CheckMate){
            //         dispChckMt.style.display = "initial";
            //     }else{
            //         dispChckMt.style.display = "none";
            //     }
            //     val.style.background = 'red';
            //     highlights.push(val);
            // }
    }
    prev = placeId;
}
  
}


this.kingMovement = function(controlId){
    // console.log('in king movement');
    var kselected = document.getElementById(controlId);
    var ktype = kselected.classList[1];
    var kcolour = kselected.classList[0];
    var kplaceId = kselected.parentNode.id;
    //var dude = document.getElementById('r1D');
    //console.log('dude: '+dude.innerHTML);
    var Iking = 0;
    var Jking = 0;
    var kfreeAreas = [];
    //console.log('king type: '+ktype);
    for(var i=0; i<8; i++){
        for(var j=0; j<8; j++){
      
            //console.log('has piece: '+square.firstChild);
            if(kplaceId==boardMatrix[i][j]){
                Iking = i;
                Jking = j;
                break;
            }
        }
    }
    //console.log("king movement");
    localStorage.setItem("CompInCheck", "N");
    localStorage.setItem("CompNWInCheck", "N");
    localStorage.setItem("CompNEInCheck", "N");
    localStorage.setItem("CompSWInCheck", "N");
    localStorage.setItem("CompSEInCheck", "N");
    localStorage.setItem("CompUpInCheck", "N");
    localStorage.setItem("CompDownInCheck", "N");
    localStorage.setItem("CompRightInCheck", "N");
    localStorage.setItem("CompLeftInCheck", "N");

    localStorage.setItem("CheckMate", "N");
    

    localStorage.setItem("CurrentDirectionArray", JSON.stringify([]));
    localStorage.setItem("CurrentAttackerArray", JSON.stringify([]));
    localStorage.setItem("SaverArray", JSON.stringify([]));
    localStorage.setItem("AttackerArray", JSON.stringify([]));
    localStorage.setItem("InGuard", "N");
    localStorage.setItem("PieceInGuard", "");
    localStorage.setItem("FreeMovementLength", "");
    localStorage.setItem("CanSaveKing", "N");

    if(freeMov){
        localStorage.setItem("FreeMov", "Y");
    }else{
        localStorage.setItem("FreeMov", "N");
    }

    if(ktype=='king'){ 
        // console.log('hello king: ');
        if([Iking+1]<8&&[Jking-1]>-1){
            var seCheck = false;
            var val = document.getElementById(boardMatrix[Iking+1][Jking-1]);
            var pieceArr = isChecked(boardMatrix[Iking+1][Jking-1], piecesFoundnw);
            for(var b=0; b<pieceArr.length; b++){
                seCheck = canCheck(pieceArr[b], boardMatrix[Iking+1][Jking-1]);
                //console.log('nw check');
                if(seCheck){
                    localStorage.setItem("CompSEInCheck", "Y");
                    break;
                }
                //console.log('is checked: '+b+' '+nwCheck);
            }
            //console.log('pieces: '+pieceArr);

            if(seCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[Iking+1][Jking-1]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!seCheck&&!val.hasChildNodes()){
                kfreeAreas.push(boardMatrix[Iking+1][Jking-1]); 
            }
            
        }
        if([Iking+1]<8){
            var downCheck = false;
            var pieceArr = isChecked(boardMatrix[Iking+1][Jking], piecesFoundup);
            //console.log('wats up dude');
            var val = document.getElementById(boardMatrix[Iking+1][Jking]);
            for(var b=0; b<pieceArr.length; b++){
                dowmCheck = canCheck(pieceArr[b], boardMatrix[Iking+1][Jking]);
                //console.log('up check');
                if(downCheck){
                    localStorage.setItem("CompDownInCheck", "Y");
                    break;
                }
            }
            if(downCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[Iking+1][Jking]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!downCheck&&!val.hasChildNodes()){
                kfreeAreas.push(boardMatrix[Iking+1][Jking]);  
            }
            
        }    
        if([Iking+1]<8&&[Jking+1]<8){
            //console.log("king ne: "+boardMatrix[Iking+1][Jking+1])
            var swCheck = false;
            var pieceArr = isChecked(boardMatrix[Iking+1][Jking+1], piecesFoundne);
            var val = document.getElementById(boardMatrix[Iking+1][Jking+1]);
            for(var b=0; b<pieceArr.length; b++){
                swCheck = canCheck(pieceArr[b], boardMatrix[Iking+1][Jking+1]);
                
                if(swCheck){
                    localStorage.setItem("CompSWInCheck", "Y");
                    break;
                }
                //console.log('is checked: '+pieceArr[b]+' - '+neCheck);
            }
            if(swCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[Iking+1][Jking+1]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!swCheck&&!val.hasChildNodes()){
                kfreeAreas.push(boardMatrix[Iking+1][Jking+1]);
            }
            
        }
        if([Jking-1]>-1){
            var rightCheck = false;
            var pieceArr = isChecked(boardMatrix[Iking][Jking-1], piecesFoundleft);
            var val = document.getElementById(boardMatrix[Iking][Jking-1]);
            for(var b=0; b<pieceArr.length; b++){
                rightCheck = canCheck(pieceArr[b], boardMatrix[Iking][Jking-1]);
                
                if(rightCheck){
                    localStorage.setItem("CompRightInCheck", "Y");
                    break;
                }
                //console.log('is checked: '+b+' '+leftCheck);
            }
            //console.log('left check');
            if(rightCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[Iking][Jking-1]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!rightCheck&&!val.hasChildNodes()){
                kfreeAreas.push(boardMatrix[Iking][Jking-1]);  
            }
            
        }
        if([Jking+1]<8){
            var leftCheck = false;
            var pieceArr = isChecked(boardMatrix[Iking][Jking+1], piecesFoundright);
            var val = document.getElementById(boardMatrix[Iking][Jking+1]);
            for(var b=0; b<pieceArr.length; b++){
                leftCheck = canCheck(pieceArr[b], boardMatrix[Iking][Jking+1]);
                //console.log('right check: '+b+' '+pieceArr[b]);
                if(leftCheck){
                    localStorage.setItem("CompLeftInCheck", "Y");
                    break;
                }
                //console.log('is checked: '+b+' '+rightCheck);
            }
            //console.log('right check');
            if(leftCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[Iking][Jking+1]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!leftCheck&&!val.hasChildNodes()){
                kfreeAreas.push(boardMatrix[Iking][Jking+1]);
            }
            
        }
        if([Iking-1]>-1&&[Jking-1]!=-1){
            var neCheck = false;
            var pieceArr = isChecked(boardMatrix[Iking-1][Jking-1], piecesFoundsw);
            var val = document.getElementById(boardMatrix[Iking-1][Jking-1]);
            for(var b=0; b<pieceArr.length; b++){
                neCheck = canCheck(pieceArr[b], boardMatrix[Iking-1][Jking-1]);
                //console.log('sw check');
                if(neCheck){
                    //console.log("hello ne check: "+neCheck);
                    localStorage.setItem("CompNEInCheck", "Y");
                    break;
                }
                //console.log('is checked: '+b+' '+swCheck);
            }
            if(neCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[Iking-1][Jking-1]);
                val.style.background = 'orange'; 
                highlights.push(val);
            }else if(!neCheck&&!val.hasChildNodes()){
                kfreeAreas.push(boardMatrix[Iking-1][Jking-1]);  
            }
            
        }
        if([Iking-1]>-1){
            var upCheck = false;
            var pieceArr = isChecked(boardMatrix[Iking-1][Jking], piecesFounddown);
            var val = document.getElementById(boardMatrix[Iking-1][Jking]);
            for(var b=0; b<pieceArr.length; b++){
                upCheck = canCheck(pieceArr[b], boardMatrix[Iking-1][Jking]);
                //console.log('down check');
                 if(upCheck){
                    localStorage.setItem("CompUpInCheck", "Y");
                    break;
                }
                //console.log('is checked: '+b+' '+downCheck);
            }
            if(upCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[Iking-1][Jking]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!upCheck&&!val.hasChildNodes()){
                //kingsArray.push(boardMatrix[Iking-1][Jking]);
                //allIdArr.push(boardMatrix[Iking-1][Jking]);
                kfreeAreas.push(boardMatrix[Iking-1][Jking]);
                // val = document.getElementById(boardMatrix[Iking-1][Jking]);
                // //val.style.background = 'blue';
                // highlights.push(val);    
            }
            
        }
        if([Iking-1]>-1&&[Jking+1]<8){
            var nwCheck = false;
            var pieceArr = isChecked(boardMatrix[Iking-1][Jking+1], piecesFoundse);
            var val = document.getElementById(boardMatrix[Iking-1][Jking+1]);
            for(var b=0; b<pieceArr.length; b++){
                nwCheck = canCheck(pieceArr[b], boardMatrix[Iking-1][Jking+1]);
                //console.log('se check');
                if(nwCheck){
                    localStorage.setItem("CompNWInCheck", "Y");
                    break;
                }
                //console.log('is checked: '+b+' '+seCheck);
            }
            if(nwCheck&&!val.hasChildNodes()){
                val = document.getElementById(boardMatrix[Iking-1][Jking+1]);
                val.style.background = 'orange';
                highlights.push(val);
            }else if(!nwCheck&&!val.hasChildNodes()){
                kfreeAreas.push(boardMatrix[Iking-1][Jking+1]);  
            }
            
        }
            
            
            var canReach = false;
            inCheck = false;
            isGuard = false;
            var checked = false;
            checkArr = [];
            var pieceAr = kingIsChecked(boardMatrix[Iking][Jking], piecesChecking);
            // console.log("pieceAr: "+pieceAr);
            checkArr = pieceAr;
            var val = document.getElementById(boardMatrix[Iking][Jking]);
            for(var b=0; b<pieceAr.length; b++){
                canReach = kingCanCheck(pieceAr[b], boardMatrix[Iking][Jking]);
                if(canReach){
                    reachable.push(pieceAr[b]);
                    // console.log("reachable: "+pieceAr[b]);
                }
            }
            var a = undefined;
            for(var r=0; r<reachable.length; r++){
                val = document.getElementById(boardMatrix[Iking][Jking]);
                var tempAt = document.getElementById(reachable[r]);
                var nextAt = tempAt.parentNode.id;
                attackerArr.push(nextAt);
                inCheck = finalCanCheck(reachable[r], boardMatrix[Iking][Jking]);
                // console.log("reachable vals: "+reachable[r]);
                if(inCheck){
                    localStorage.setItem("CompInCheck", "Y");
                    kcanSaveKing =  trySave();
                    var tempcansave =  tryGet(Iking, Jking);
                    if(!kcanSaveKing){
                        kcanSaveKing = tempcansave;
                    } 
                    val.style.background = 'red';
                    highlights.push(val);
                    checked = true;          
                    break;
                }
            }

            if(kcanSaveKing){
                localStorage.setItem("CanSaveKing", "Y");
            }else{
                localStorage.setItem("CanSaveKing", "N");
            }

            localStorage.setItem("FreeMovementLength", ""+kfreeAreas.length);
            if(checked){
                localStorage.setItem("CurrentDirectionArray", JSON.stringify(currDir));
                localStorage.setItem("CurrentAttackerArray", JSON.stringify(attackerArr));
                localStorage.setItem("SaverArray", JSON.stringify(savers));
                localStorage.setItem("AttackerArray", JSON.stringify(attackers));
            }
            //console.log("can save: "+kcanSaveKing);
            if(checked&&!kcanSaveKing){
                //console.log("freeareas: "+kfreeAreas.length==0);
                if(kfreeAreas.length==0){
                    kCheckMate = true;
                    //console.log("hello checkmate");
                }else{
                    kCheckMate = false;
                }
                dispChckMt = document.getElementById("checkmate");
                if(kCheckMate){
                    dispChckMt.style.display = "initial";
                    localStorage.setItem("CheckMate", "Y");
                }else{
                    dispChckMt.style.display = "none";
                    localStorage.setItem("CheckMate", "N");
                }
            }
            // console.log("latest: "+latestVal+" - "+placeId);
            //localStorage.setItem("PieceInGuard", latestVal);
            if(latestVal!=''&&latestVal!=boardMatrix[Iking][Jking]&&latestVal==placeId&&!inCheck){
                isGuard = true;
                //localStorage.setItem("InGuard", "Y");
            }else{
                isGuard = false;
                //localStorage.setItem("InGuard", "N");
            }
    }
}

function trySave(){
    var isSet = false;
    var tscanSaveKing = false;
    for(var n=0; n<currDir.length-1; n++){
        var cd = document.getElementById(currDir[n]);
        cd.style.background = 'green';
        highlights.push(cd);
        var a = getCanSave(currDir[n]);
        for(var i=0; i<a.length; i++){   
            nonrepeatArr(a[i]);
        }
        //console.log("tsarr: "+pcarr);
        if(!isSet){
            for(var l=0; l<pcarr.length; l++){
                tscanSaveKing = canSave(pcarr[l], currDir[n]);
                //console.log("ts can save: "+tscanSaveKing);
                if(tscanSaveKing&&pcarr[l]!='bking'){   
                    var hcd = document.getElementById(pcarr[l]);
                    savers.push(pcarr[l]);
                    var phcd = hcd.parentNode;
                    phcd.style.background = 'purple';
                    highlights.push(phcd);
                    isSet = true;
                    break;
                }
            }
        }
    }
    return tscanSaveKing;
}

function tryGet(b, j){
    var tgcanSaveKing = false;
    var isSet = false;
    for(var n=0; n<attackerArr.length; n++){
        var cd = document.getElementById(attackerArr[n]);
        cd.style.background = '#00FA9A';
        highlights.push(cd);
        var a = getCanSave(attackerArr[n]);
        for(var i=0; i<a.length; i++){   
            nonrepeatgetArr(a[i]);

        }
        if(!isSet){
            for(var l=0; l<pgarr.length; l++){
                tgcanSaveKing = canGet(pgarr[l], attackerArr[n]);
                if(tgcanSaveKing&&pgarr[l]!='bking'){   
                    var hcd = document.getElementById(pgarr[l]);
                    attackers.push(pgarr[l]);
                    var phcd = hcd.parentNode;
                    phcd.style.background = 'mediumslateblue';
                    highlights.push(phcd);
                    isSet = true;
                    break;
                }

                if(pgarr[l]=='bking'){
                    kingCanSaveKing = kingGet(b, j);
                    if(kingCanSaveKing){
                        var hcd = document.getElementById(pgarr[l]);
                        attackers.push(pgarr[l]);
                        var phcd = hcd.parentNode;
                        phcd.style.background = 'mediumslateblue';
                        highlights.push(phcd);
                        isSet = true;
                        break;
                    }
                }
            }
        }
    }
    if(tgcanSaveKing||kingCanSaveKing){
        return true;
    }else{
        return false;
    }  
}

function toPlaceId(pieceArray){
    var idArr = [];
    for(var i=0; i<pieceArray.length; i++){
        var itemp = document.getElementById(pieceArray[i]);
        var itemId = itemp.parentNode.id;
        //console.log("place: "+itemId);
        idArr.push(itemId);
    }
    return idArr;
}

function nonrepeatArr(controlId){
    var isIn = false;
    for(var i=0; i<pcarr.length; i++){
        if(controlId==pcarr[i]){
            isIn = true;
            //console.log("item found");   
        }
    }
    if(!isIn){
        pcarr.push(controlId);
        //console.log("add to arr"); 
    }
}

function nonrepeatremovedArr(controlId){
    var isIn = false;
    for(var i=0; i<nestedPieceIds.length; i++){
        if(controlId==nestedPieceIds[i]){
            isIn = true;
            //console.log("item found");   
        }
    }
    if(!isIn){
        nestedPieceIds.push(controlId);
        //console.log("add to arr"); 
    }
}

function nonrepeatgetArr(controlId){
    var isIn = false;
    for(var i=0; i<pgarr.length; i++){
        if(controlId==pgarr[i]){
            isIn = true;
            //console.log("item found");   
        }
    }
    if(!isIn){
        pgarr.push(controlId);
        //console.log("add to arr"); 
    }
}

function kingGet(i, j){
    var Ikg = i;
    var Jkg = j;
    var kingCanGet = false;
    //console.log("in kingGet: "+kingCanGet+" pos: "+boardMatrix[Ikg][Jkg]);
    if([Ikg+1]<8&&[Jkg-1]>-1){
        var pos = document.getElementById(boardMatrix[Ikg+1][Jkg-1]);
        if(pos!=null){
            if(pos.hasChildNodes()){
                var item = pos.firstElementChild;
                var itemColour = item.classList[0];
                if(itemColour==oppColour){
                    kingCanGet = true;
                    return kingCanGet; 
                }
            }
        }
    }
    if([Ikg+1]<8){
        var pos = document.getElementById(boardMatrix[Ikg+1][Jkg]);
        if(pos!=null){
            if(pos.hasChildNodes()){
                var item = pos.firstElementChild;
                var itemColour = item.classList[0];
                if(itemColour==oppColour){
                   kingCanGet = true;
                   return kingCanGet; 
               }
           }
        }
    }    
    if([Ikg+1]<8&&[Jkg+1]<8){
        //console.log("in top right "+boardMatrix[Ikg+1][Jkg+1]);
        var pos = document.getElementById(boardMatrix[Ikg+1][Jkg+1]);
        if(pos!=null){
            //console.log("in top right pos not null "+boardMatrix[Ikg+1][Jkg+1]+' '+pos.hasChildNodes());
            if(pos.hasChildNodes()){
                var item = pos.firstElementChild;
                var itemColour = item.classList[0];
                //console.log("in top right true"+boardMatrix[Ikg+1][Jkg+1]+' '+kingCanGet);
                if(itemColour==oppColour){
                   kingCanGet = true;
                   return kingCanGet; 
               }
           }
        }
    }
    if([Jkg-1]>-1){
        var pos = document.getElementById(boardMatrix[Ikg][Jkg-1]);
        if(pos!=null){
            if(pos.hasChildNodes()){
                var item = pos.firstElementChild;
                var itemColour = item.classList[0];
                if(itemColour==oppColour){
                   kingCanGet = true;
                   return kingCanGet; 
               }
           }
        }
    }
    if([Jkg+1]<8){
        var pos = document.getElementById(boardMatrix[Ikg][Jkg+1]);
        if(pos!=null){
            if(pos.hasChildNodes()){
               var item = pos.firstElementChild;
               var itemColour = item.classList[0];
                if(itemColour==oppColour){
                    kingCanGet = true;
                    return kingCanGet; 
                }
            }
        }
    }
    if([Ikg-1]>-1&&[Jkg-1]!=-1){
        var pos = document.getElementById(boardMatrix[Ikg-1][Jkg-1]);
        if(pos!=null){
            if(pos.hasChildNodes()){
                var item = pos.firstElementChild;
                var itemColour = item.classList[0];
                if(itemColour==oppColour){
                   kingCanGet = true;
                   return kingCanGet; 
               }
            }
        }
    }
    if([Ikg-1]>-1){
        var pos = document.getElementById(boardMatrix[Ikg-1][Jkg]);
        if(pos!=null){
            if(pos.hasChildNodes()){
                var item = pos.firstElementChild;
                var itemColour = item.classList[0];
                if(itemColour==oppColour){
                   kingCanGet = true;
                   return kingCanGet; 
               }
           }
        }
    }
    if([Ikg-1]>-1&&[Jkg+1]<8){
        var pos = document.getElementById(boardMatrix[Ikg-1][Jkg+1]);
        if(pos!=null){
            if(pos.hasChildNodes()){
               var item = pos.firstElementChild;
               var itemColour = item.classList[0];
               if(itemColour==oppColour){
                   kingCanGet = true;
                   return kingCanGet; 
                }
            }
        }
    }        
}

function isChecked(controlId, piecesFound){
    var control = document.getElementById(controlId);
    var piecesFound = [];
    var horseArrk = [];
    var kingsArrayk = [];
    var nwArrk = [];
    var neArrk = [];
    var swArrk = [];
    var seArrk = [];
    var Ik = 0;
    var Jk = 0;
    
    for(var i=0; i<8; i++){
        for(var j=0; j<8; j++){
      
            //console.log('has piece: '+square.firstChild);
            if(controlId==boardMatrix[i][j]){
                Ik = i;
                Jk = j;
                break;
            }
        }
    }  
    var leftk = Jk;
    var rightk = Jk;
    var upk = Ik;
    var downk = Ik;


    
    
    var nwleftk = Jk;
    var nwupk = Ik;
    var nerightk = Jk;
    var neupk = Ik;
    var serightk = Jk;
    var sedownk = Ik;
    var swleftk = Jk;
    var swdownk = Ik;




    var leftsk = document.getElementById(boardMatrix[Ik][Jk]);
    var rightsk = document.getElementById(boardMatrix[Ik][Jk]);
    var upsk = document.getElementById(boardMatrix[Ik][Jk]);
    var downsk = document.getElementById(boardMatrix[Ik][Jk]);

    var nwk = document.getElementById(boardMatrix[Ik][Jk]);
    var nek = document.getElementById(boardMatrix[Ik][Jk]);  
    var swk = document.getElementById(boardMatrix[Ik][Jk]);
    var sek = document.getElementById(boardMatrix[Ik][Jk]);


    var pawntrk = '';
    var pawntlk = '';
    var typeFound = '';
   
      
     //initialises objects each time
    function movable(){
        var rstart = false;
        var lstart = false;
        var ustart = false;
        var dstart = false;


        var nwstart = false;
        var nestart = false;
        var swstart = false;
        var sestart = false;
        //console.log("MOVEABLE");
        for(var i=0; i<8; i++){
            if(rightk>-1){
                rightsk = document.getElementById(boardMatrix[Ik][rightk]); 
            }if(leftk<8){
                leftsk = document.getElementById(boardMatrix[Ik][leftk]);  
            }if(upk>-1){
                upsk = document.getElementById(boardMatrix[upk][Jk]); 
            }if(downk<8){
                downsk = document.getElementById(boardMatrix[downk][Jk]);
            }
           
            if(rightk<8&&rightk>-1){
                if(rightsk!=null){
                    if(!rightsk.firstElementChild||!rstart){
                        rightk--;
                        rstart = true;
                    }
                }
            }
            if(leftk>-1&&leftk<8){
                if(leftsk!=null){
                    if(!leftsk.firstElementChild||!lstart){
                        leftk++;
                        lstart = true;
                    }
                }
            }
            if(upk<8&&upk>-1){
                if(upsk!=null){
                    if(!upsk.firstElementChild||!ustart){
                        upk--;
                        //console.log('hello up: '+up+' - '+ups);
                        ustart = true;
                    }
                }
            }
            if(downk>-1&&downk<8){
                if(downsk!=null){
                    if(!downsk.firstElementChild||!dstart){
                        downk++;
                        dstart = true;
                    }
                }
            }
                if(nwleftk<8&&nwupk>-1){
                    nwk = document.getElementById(boardMatrix[nwupk][nwleftk]);
                    nwArrk.push(nwk);          
                }if(nerightk>-1&&neupk>-1){
                    nek = document.getElementById(boardMatrix[neupk][nerightk]);
                    neArrk.push(nek);     
                }if(swleftk<8&&swdownk<8){
                    swk = document.getElementById(boardMatrix[swdownk][swleftk]);
                    swArrk.push(swk);
                }if(serightk>-1&&sedownk<8){
                    sek = document.getElementById(boardMatrix[sedownk][serightk]);
                    seArrk.push(sek);  
                }         

                if(nwleftk<8&&nwupk>-1){
                    if(nwk!=null){
                        if(!nwk.firstElementChild||!nwstart){
                            nwleftk++;
                            nwupk--;
                            nwstart = true;
                        }     
                    }
                }
                if(nerightk>-1&&neupk>-1){
                    if(nek!=null){
                        if(!nek.firstElementChild||!nestart){
                            nerightk--;
                            neupk--;
                            nestart = true;
                        }
                    }
                }
                if(swleftk<8&&swdownk<8){
                    if(swk!=null){
                        if(!swk.firstElementChild||!swstart){
                            swleftk++;
                            swdownk++;
                            swstart = true;
                        }
                    }
                }
                if(serightk>-1&&sedownk<8){
                    if(sek!=null){
                        if(!sek.firstElementChild||!sestart){
                            serightk--;
                            sedownk++;
                            sestart = true;
                        } 
                    }
                }
                
        }     
    }
    movable();
    //console.log('colour: '+colour);
    if(rightsk!=null){
        if(rightsk.hasChildNodes()){
            var val = rightsk.firstElementChild;
            //var theColour = val.classList[0];
            //console.log('the colour: '+theColour);
            if(val!=null){
                if(val.classList[0]==oppColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('r: '+rightsk.id);
                }
            }
        } 
    }
    if(leftsk!=null){
        if(leftsk.hasChildNodes()){
            var val = leftsk.firstElementChild;
            //var theColour = val.classList[0];
            if(val!=null){
                if(val.classList[0]==oppColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('l: '+leftsk.id);
                }
            } 
        }
    } 

    if(upsk!=null){
        if(upsk.hasChildNodes()){
            var val = upsk.firstElementChild;
            //var theColour = val.classList[0];
            //console.log('up val: '+val.classList[0]);
            if(val!=null){
                if(val.classList[0]==oppColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('u: '+upsk.id);
                }
            } 
        }
    } 

    if(downsk!=null){
        if(downsk.hasChildNodes()){
            var val = downsk.firstElementChild;
            //var theColour = val.classList[0];
            if(val!=null){
                if(val.classList[0]==oppColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('d: '+downsk.id);
                }
            } 
        }
    } 
    if(nwk!=null){
        if(nwk.hasChildNodes()){
            var val = nwk.firstElementChild;
            //var theColour = val.classList[0];
            if(val!=null){
                if(val.classList[0]==oppColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('nw: '+nwk.id);
                }
            } 
        }
    } 

    if(nek!=null){
        if(nek.hasChildNodes()){
            var val = nek.firstElementChild;
            //var theColour = val.classList[0];
            if(val!=null){
                if(val.classList[0]==oppColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('ne: '+nek.id);
                }
            } 
        }       
    } 

    if(swk!=null){
        //console.log('place: '+swk.id);
        if(swk.hasChildNodes()){
            var val = swk.firstElementChild;
            if(val!=null){
                if(val.classList[0]==oppColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('sw: '+swk.id);
                }
            } 
        }
    } 

    if(sek!=null){
        if(sek.hasChildNodes()){
            var val = sek.firstElementChild;
            if(val!=null){
                if(val.classList[0]==oppColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('se: '+sek.id);
                }
            } 
        }
    }   

    if(Ik-1>-1&&Jk-1>-1){
        pawntrk = document.getElementById(boardMatrix[Ik-1][Jk-1]);
        if(pawntrk.hasChildNodes()){
            var val = pawntrk.firstElementChild;
            if(val!=null){
                if(val.classList[0]==oppColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                }
            }
        } 
    }
    if(Ik-1>-1&&Jk+1<8){
        pawntlk = document.getElementById(boardMatrix[Ik-1][Jk+1]);
        if(pawntlk.hasChildNodes()){
            var val = pawntlk.firstElementChild;
            //var theColour = val.classList[0];
            if(val!=null){
                if(val.classList[0]==oppColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                }
            } 
        } 
    }

    //if(type=='horse'){
        
        if([Ik+2]<8&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik+2][Jk-1]);
        }
        if([Ik+2]<8&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik+2][Jk+1]);
        }
        if([Ik+1]<8&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik+1][Jk+2]);
        }
        if([Ik-1]>-1&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik-1][Jk+2]);
        }
        if([Ik-2]>-1&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik-2][Jk+1]);
        }
        if([Ik-2]>-1&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik-2][Jk-1]);
        }
        if([Ik+1]<8&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik+1][Jk-2]);
        }
        if([Ik-1]>-1&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik-1][Jk-2]);
        }
        //console.log('in horse arr: '+horseArr);
    //}

    for(var t=0; t<horseArrk.length; t++){
        //console.log('horse: '+horseArrk[t]);
        nextHorse = document.getElementById(horseArrk[t]);
        if(nextHorse.hasChildNodes()){
            var elem = document.getElementById(horseArrk[t]);
            var val = elem.firstElementChild;
            
                //var theColour = val.classList[0];
                if(val!=null){
                    if(val.classList[0]==oppColour&&val.classList[0]!=null){
                        piecesFound.push(val.id);
                    }
                }
         
        }
    }
 
    return piecesFound;

}

function getCanSave(controlId){
    var control = document.getElementById(controlId);
    //console.log("get col: "+colour);
    var piecesFound = [];
    var horseArrk = [];
    var kingsArrayk = [];
    var nwArrk = [];
    var neArrk = [];
    var swArrk = [];
    var seArrk = [];
    var Ik = 0;
    var Jk = 0;
    
    for(var i=0; i<8; i++){
        for(var j=0; j<8; j++){
            //console.log('has piece: '+square.firstChild);
            if(controlId==boardMatrix[i][j]){
                Ik = i;
                Jk = j;
                break;
            }
        }
    }  
    var leftk = Jk;
    var rightk = Jk;
    var upk = Ik;
    var downk = Ik;

    var nwleftk = Jk;
    var nwupk = Ik;
    var nerightk = Jk;
    var neupk = Ik;
    var serightk = Jk;
    var sedownk = Ik;
    var swleftk = Jk;
    var swdownk = Ik;

    var leftsk = document.getElementById(boardMatrix[Ik][Jk]);
    var rightsk = document.getElementById(boardMatrix[Ik][Jk]);
    var upsk = document.getElementById(boardMatrix[Ik][Jk]);
    var downsk = document.getElementById(boardMatrix[Ik][Jk]);

    var nwk = document.getElementById(boardMatrix[Ik][Jk]);
    var nek = document.getElementById(boardMatrix[Ik][Jk]);  
    var swk = document.getElementById(boardMatrix[Ik][Jk]);
    var sek = document.getElementById(boardMatrix[Ik][Jk]);

    var pawntrk = '';
    var pawntlk = '';
    var typeFound = '';
     
    //initialises objects each time
    function movable(){
        var rstart = false;
        var lstart = false;
        var ustart = false;
        var dstart = false;

        var nwstart = false;
        var nestart = false;
        var swstart = false;
        var sestart = false;
        //console.log("MOVEABLE");
        for(var i=0; i<8; i++){
   
            if(rightk>-1){
                rightsk = document.getElementById(boardMatrix[Ik][rightk]); 
            }if(leftk<8){
                leftsk = document.getElementById(boardMatrix[Ik][leftk]);  
            }if(upk>-1){
                upsk = document.getElementById(boardMatrix[upk][Jk]); 
            }if(downk<8){
                downsk = document.getElementById(boardMatrix[downk][Jk]);
            }
           
            if(rightk<8&&rightk>-1){
                if(rightsk!=null){
                    if(!rightsk.firstElementChild||!rstart){
                        rightk--;
                        rstart = true;
                    }
                }
            }
            if(leftk>-1&&leftk<8){
                if(leftsk!=null){
                    if(!leftsk.firstElementChild||!lstart){
                        leftk++;
                        lstart = true;
                    }
                }
            }
            if(upk<8&&upk>-1){
                if(upsk!=null){
                    if(!upsk.firstElementChild||!ustart){
                        upk--;
                        //console.log('hello up: '+up+' - '+ups);
                        ustart = true;
                    }
                }
            }
            if(downk>-1&&downk<8){
                if(downsk!=null){
                    if(!downsk.firstElementChild||!dstart){
                        downk++;
                        dstart = true;
                    }
                }
            }
                if(nwleftk<8&&nwupk>-1){
                    nwk = document.getElementById(boardMatrix[nwupk][nwleftk]);
                    nwArrk.push(nwk);          
                }if(nerightk>-1&&neupk>-1){
                    nek = document.getElementById(boardMatrix[neupk][nerightk]);
                    neArrk.push(nek);     
                }if(swleftk<8&&swdownk<8){
                    swk = document.getElementById(boardMatrix[swdownk][swleftk]);
                    swArrk.push(swk);
                }if(serightk>-1&&sedownk<8){
                    sek = document.getElementById(boardMatrix[sedownk][serightk]);
                    seArrk.push(sek);  
                }         

                if(nwleftk<8&&nwupk>-1){
                    if(nwk!=null){
                        if(!nwk.firstElementChild||!nwstart){
                            nwleftk++;
                            nwupk--;
                            nwstart = true;
                        }     
                    }
                }
                if(nerightk>-1&&neupk>-1){
                    if(nek!=null){
                        if(!nek.firstElementChild||!nestart){
                            nerightk--;
                            neupk--;
                            nestart = true;
                        }
                    }
                }
                if(swleftk<8&&swdownk<8){
                    if(swk!=null){
                        if(!swk.firstElementChild||!swstart){
                            swleftk++;
                            swdownk++;
                            swstart = true;
                        }
                    }
                }
                if(serightk>-1&&sedownk<8){
                    if(sek!=null){
                        if(!sek.firstElementChild||!sestart){
                            serightk--;
                            sedownk++;
                            sestart = true;
                        } 
                    }
                }
                
        }   
    }
    movable();
    //console.log('colour: '+colour);
    if(rightsk!=null){
        if(rightsk.hasChildNodes()){
            var val = rightsk.firstElementChild;
            var val2 = rightsk;
            if(val!=null){
                if(val.classList[0]==setColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('r: '+rightsk.id);
                }
            }
        } 
    }
    if(leftsk!=null){
        if(leftsk.hasChildNodes()){
            var val = leftsk.firstElementChild;
            var val2 = leftsk;
            if(val!=null){
                if(val.classList[0]==setColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('l: '+leftsk.id);
                }
            } 
        }
    } 

    if(upsk!=null){
        if(upsk.hasChildNodes()){
            var val = upsk.firstElementChild;
            var val2 = upsk;
            if(val!=null){
                if(val.classList[0]==setColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('u: '+upsk.id);
                }
            } 
        }
    } 

    if(downsk!=null){
        if(downsk.hasChildNodes()){
            var val = downsk.firstElementChild;
            var val2 = downsk;
            if(val!=null){
                if(val.classList[0]==setColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('d: '+downsk.id);
                }
            } 
        }
    } 
    if(nwk!=null){
        if(nwk.hasChildNodes()){
            var val = nwk.firstElementChild;
            var val2 = nwk;
            if(val!=null){
                if(val.classList[0]==setColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('nw: '+nwk.id);
                }
            } 
        }
    } 

    if(nek!=null){
        if(nek.hasChildNodes()){
            var val = nek.firstElementChild;
            var val2 = nek;
            if(val!=null){
                if(val.classList[0]==setColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('ne: '+nek.id);
                }
            } 
        }       
    } 

    if(swk!=null){
        if(swk.hasChildNodes()){
            var val = swk.firstElementChild;
            var val2 = swk;
            if(val!=null){
                if(val.classList[0]==setColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('sw: '+swk.id);
                }
            } 
        }
    } 

    if(sek!=null){
        if(sek.hasChildNodes()){
            var val = sek.firstElementChild;
            var val2 = sek;
            if(val!=null){
                if(val.classList[0]==setColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                    //console.log('se: '+sek.id);
                }
            } 
        }
    }   

    if(Ik-1>-1&&Jk-1>-1){
        pawntrk = document.getElementById(boardMatrix[Ik-1][Jk-1]);
        if(pawntrk.hasChildNodes()){
            var val = pawntrk.firstElementChild;
            if(val!=null){
                if(val.classList[0]==setColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                }
            }
        } 
    }
    if(Ik-1>-1&&Jk+1<8){
        pawntlk = document.getElementById(boardMatrix[Ik-1][Jk+1]);
        if(pawntlk.hasChildNodes()){
            var val = pawntlk.firstElementChild;
            //var theColour = val.classList[0];
            if(val!=null){
                if(val.classList[0]==setColour&&val.classList[0]!=null){
                    piecesFound.push(val.id);
                }
            } 
        } 
    }


    //if(type=='horse'){
        
        if([Ik+2]<8&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik+2][Jk-1]);
        }
        if([Ik+2]<8&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik+2][Jk+1]);
        }
        if([Ik+1]<8&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik+1][Jk+2]);
        }
        if([Ik-1]>-1&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik-1][Jk+2]);
        }
        if([Ik-2]>-1&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik-2][Jk+1]);
        }
        if([Ik-2]>-1&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik-2][Jk-1]);
        }
        if([Ik+1]<8&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik+1][Jk-2]);
        }
        if([Ik-1]>-1&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik-1][Jk-2]);
        }
        //console.log('in horse arr: '+horseArr);
    //}

    for(var t=0; t<horseArrk.length; t++){
        //console.log('horse: '+horseArrk[t]);
        nextHorse = document.getElementById(horseArrk[t]);
        if(nextHorse.hasChildNodes()){
            var elem = document.getElementById(horseArrk[t]);
            var val = elem.firstElementChild;
            var val2 = elem;
                //var theColour = val.classList[0];
                if(val!=null){
                    if(val.classList[0]==setColour&&val.classList[0]!=null){
                        piecesFound.push(val.id);
                    }
                }
         
        }
    }
    return piecesFound;
}

function kingIsChecked(controlId, kpiecesFound){
    var control = document.getElementById(controlId);
    kingPiece = control.firstElementChild;
    kingCol = kingPiece.classList[0];
    //console.log("kingcol: "+kingCol);
    kpiecesFound = [];
    //console.log("colour: "+colour);
    var horseArrk = [];
    var kingsArrayk = [];
    var nwArrk = [];
    var neArrk = [];
    var swArrk = [];
    var seArrk = [];
    var Ik = 0;
    var Jk = 0;
    
    for(var i=0; i<8; i++){
        for(var j=0; j<8; j++){
      
            //console.log('has piece: '+square.firstChild);
            if(controlId==boardMatrix[i][j]){
                Ik = i;
                Jk = j;
                break;
            }
        }
    }  
    var leftk = Jk;
    var rightk = Jk;
    var upk = Ik;
    var downk = Ik;


    
    
    var nwleftk = Jk;
    var nwupk = Ik;
    var nerightk = Jk;
    var neupk = Ik;
    var serightk = Jk;
    var sedownk = Ik;
    var swleftk = Jk;
    var swdownk = Ik;


    
    var isNwCh = false; 
    var isNeCh = false;
    var isSwCh = false;          
    var isSeCh = false;
    var isNwCh2 = false; 
    var isNeCh2 = false;     
    var isSwCh2 = false;
    var isSeCh2 = false;

    var leftsk = document.getElementById(boardMatrix[Ik][Jk]);
    var rightsk = document.getElementById(boardMatrix[Ik][Jk]);
    var upsk = document.getElementById(boardMatrix[Ik][Jk]);
    var downsk = document.getElementById(boardMatrix[Ik][Jk]);

    var nwk = document.getElementById(boardMatrix[Ik][Jk]);
    var nek = document.getElementById(boardMatrix[Ik][Jk]);  
    var swk = document.getElementById(boardMatrix[Ik][Jk]);
    var sek = document.getElementById(boardMatrix[Ik][Jk]);


    var pawntrk = '';
    var pawntlk = '';
    var typeFound = '';
   
      
     //initialises objects each time
    function movable(){
        var rstart = false;
        var lstart = false;
        var ustart = false;
        var dstart = false;


        var nwstart = false;
        var nestart = false;
        var swstart = false;
        var sestart = false;
        //console.log("MOVEABLE");
        for(var i=0; i<8; i++){

           
            if(rightk>-1){
                rightsk = document.getElementById(boardMatrix[Ik][rightk]); 
            }if(leftk<8){
                leftsk = document.getElementById(boardMatrix[Ik][leftk]);  
            }if(upk>-1){
                upsk = document.getElementById(boardMatrix[upk][Jk]); 
                //console.log("upsk id: "+upsk.id);
            }if(downk<8){
                downsk = document.getElementById(boardMatrix[downk][Jk]);
            }
                    
                    
                    
           
           if(rightk>-1){
                if(rightsk!=null){
                    ropp = true;
                    if(rightsk.firstElementChild){
                        val = rightsk.firstElementChild;
                        if(val.classList[0]==kingCol){
                            ropp = false;
                        }
                    }
                    if(!rightsk.firstElementChild||!rstart||!ropp){
                        rightk--;
                        rstart = true;
                        ropp = true;
                    }
                }
            }
            if(leftk<8){
                if(leftsk!=null){
                    lopp = true;
                    if(leftsk.firstElementChild){
                        val = leftsk.firstElementChild;
                        if(val.classList[0]==kingCol){
                            lopp = false;
                        }
                    }
                    if(!leftsk.firstElementChild||!lstart||!lopp){
                        leftk++;
                        lstart = true;
                        lopp = true;
                    }
                }
            }
            if(upk>-1){
                if(upsk!=null){
                    uopp = true;
                    if(upsk.firstElementChild){
                        val = upsk.firstElementChild;
                        if(val.classList[0]==kingCol){
                            uopp = false;
                        }
                    }
                    if(!upsk.firstElementChild||!ustart||!uopp){
                        upk--;
                        ustart = true;
                        uopp = true;
                    }
                }
            }
            if(downk<8){
                if(downsk!=null){
                    dopp = true;
                    if(downsk.firstElementChild){
                        val = downsk.firstElementChild;
                        if(val.classList[0]==kingCol){
                            dopp = false;
                        }
                    }
                    if(!downsk.firstElementChild||!dstart||!dopp){
                        downk++;
                        dstart = true;
                        dopp = true;
                    }
                }
            }
    
                if(nwleftk<8&&nwupk>-1){
                    nwk = document.getElementById(boardMatrix[nwupk][nwleftk]);
                    nwArrk.push(nwk);          
                }if(nerightk>-1&&neupk>-1){
                    nek = document.getElementById(boardMatrix[neupk][nerightk]);
                    neArrk.push(nek);     
                }if(swleftk<8&&swdownk<8){
                    swk = document.getElementById(boardMatrix[swdownk][swleftk]);
                    swArrk.push(swk);
                }if(serightk>-1&&sedownk<8){
                    sek = document.getElementById(boardMatrix[sedownk][serightk]);
                    seArrk.push(sek);  
                }         
                
                if(nwleftk<8&&nwupk>-1){
                    if(nwk!=null){
                        nwopp = true;
                        if(nwk.firstElementChild){
                            val = nwk.firstElementChild;
                            if(val.classList[0]==kingCol){
                                nwopp = false;
                            }
                        }
                        if(!nwk.firstElementChild||!nwstart||!nwopp){
                            nwleftk++;
                            nwupk--;
                            nwstart = true;
                            nwopp = true;
                        }     
                    }
                }
                if(nerightk>-1&&neupk>-1){
                    if(nek!=null){
                        neopp = true;
                        if(nek.firstElementChild){
                            val = nek.firstElementChild;
                            if(val.classList[0]==kingCol){
                                neopp = false;
                            }
                        }
                        if(!nek.firstElementChild||!nestart||!neopp){
                            nerightk--;
                            neupk--;
                            nestart = true;
                            neopp = true;
                        }
                    }
                }
                if(swleftk<8&&swdownk<8){
                    if(swk!=null){
                        swopp = true;
                        if(swk.firstElementChild){
                            val = swk.firstElementChild;
                            if(val.classList[0]==kingCol){
                                swopp = false;
                            }
                        }
                        if(!swk.firstElementChild||!swstart||!swopp){
                            swleftk++;
                            swdownk++;
                            swstart = true;
                            swopp = true;
                        }
                    }
                }
                if(serightk>-1&&sedownk<8){
                    if(sek!=null){
                        seopp = true;
                        if(sek.firstElementChild){
                            val = sek.firstElementChild;
                            if(val.classList[0]==kingCol){
                                seopp = false;
                            }
                        }
                        if(!sek.firstElementChild||!sestart||!seopp){
                            serightk--;
                            sedownk++;
                            sestart = true;
                            seopp = true;
                        } 
                    }
                }         
        }     
    }
    movable();
    if(rightsk!=null){
        if(rightsk.hasChildNodes()){
            var val = rightsk.firstElementChild;
            if(val!=null){
                if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                    kpiecesFound.push(val.id);
                }
            }
        } 
    }
    if(leftsk!=null){
        if(leftsk.hasChildNodes()){
            var val = leftsk.firstElementChild;
            if(val!=null){
                if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                    kpiecesFound.push(val.id);
                }
            } 
        }
    } 

    if(upsk!=null){
        if(upsk.hasChildNodes()){
            var val = upsk.firstElementChild;
            if(val!=null){
                if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                    //console.log("up val: "+val.id+" -"+val.classList[0]+" - "+colour);
                    kpiecesFound.push(val.id);
                }
            } 
        }
    } 

    if(downsk!=null){
        if(downsk.hasChildNodes()){
            var val = downsk.firstElementChild;
            //var theColour = val.classList[0];
            if(val!=null){
                if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                    kpiecesFound.push(val.id);
                    //console.log('d: '+downsk.id);
                }
            } 
        }
    } 
    if(nwk!=null){
        if(nwk.hasChildNodes()){
            var val = nwk.firstElementChild;
            //var theColour = val.classList[0];
            if(val!=null){
                if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                    kpiecesFound.push(val.id);
                    //console.log('nw: '+nwk.id);
                }
            } 
        }
    } 

    if(nek!=null){
        if(nek.hasChildNodes()){
            var val = nek.firstElementChild;
            //var theColour = val.classList[0];
            if(val!=null){
                if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                    kpiecesFound.push(val.id);
                    //console.log('ne: '+nek.id);
                }
            } 
        }       
    } 

    if(swk!=null){
        if(swk.hasChildNodes()){
            var val = swk.firstElementChild;
            if(val!=null){
                if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                    kpiecesFound.push(val.id);
                    //console.log('sw: '+swk.id);
                }
            } 
        }
    } 

    if(sek!=null){
        if(sek.hasChildNodes()){
            var val = sek.firstElementChild;
            if(val!=null){
                if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                    kpiecesFound.push(val.id);
                    //console.log('se: '+sek.id);
                }
            } 
        }
    }   

    if(Ik-1>-1&&Jk-1>-1){
        pawntrk = document.getElementById(boardMatrix[Ik-1][Jk-1]);
        if(pawntrk.hasChildNodes()){
            var val = pawntrk.firstElementChild;
            if(val!=null){
                if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                    //console.log("pawntr color: "+val.id+" - "+val.classList[0]+" - "+colour);
                    kpiecesFound.push(val.id);
                }
            }
        } 
    }
    if(Ik-1>-1&&Jk+1<8){
        pawntlk = document.getElementById(boardMatrix[Ik-1][Jk+1]);
        if(pawntlk.hasChildNodes()){
            var val = pawntlk.firstElementChild;
            //var theColour = val.classList[0];
            if(val!=null){
                if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                    //console.log("pawntl color: "+val.id+" - "+val.classList[0]+" - "+colour);
                    kpiecesFound.push(val.id);
                }
            } 
        } 
    }


    //if(type=='horse'){
        
        if([Ik+2]<8&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik+2][Jk-1]);
        }
        if([Ik+2]<8&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik+2][Jk+1]);
        }
        if([Ik+1]<8&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik+1][Jk+2]);
        }
        if([Ik-1]>-1&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik-1][Jk+2]);
        }
        if([Ik-2]>-1&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik-2][Jk+1]);
        }
        if([Ik-2]>-1&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik-2][Jk-1]);
        }
        if([Ik+1]<8&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik+1][Jk-2]);
        }
        if([Ik-1]>-1&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik-1][Jk-2]);
        }
        //console.log('in horse arr: '+horseArr);
    //}

    for(var t=0; t<horseArrk.length; t++){
        //console.log('horse: '+horseArrk[t]);
        nextHorse = document.getElementById(horseArrk[t]);
        if(nextHorse.hasChildNodes()){
            var elem = document.getElementById(horseArrk[t]);
            var val = elem.firstElementChild;
            if(val!=null){
                //var theColour = val.classList[0];
                if(val!=null){
                    if(val.classList[0]!=kingCol&&val.classList[0]!=null){
                        kpiecesFound.push(val.id);
                    }
                }
            } 
        }
    }
    // for(var r=0; r<kpiecesFound.length; r++){
    //    console.log('piecesFound: '+kpiecesFound[r]);
    // }
    return kpiecesFound;

}


function canCheck(controlId, posId){
    var control = document.getElementById(controlId);
    var theType = control.classList[1];
    var checkColour = control.classList[0];
    var thePlaceId = control.parentNode.id;
    //console.log('attcking piece: '+thePlaceId);
    //console.log('checker type: '+theType+' checkColour: '+checkColour+' id: '+controlId+' colour '+colour);
    var horseArrk = [];
    var kingsArrayk = [];
    var nwArrk = [];
    var neArrk = [];
    var swArrk = [];
    var seArrk = [];
    var Ik = 0;
    var Jk = 0;

    for(var i=0; i<8; i++){
        for(var j=0; j<8; j++){
            if(thePlaceId==boardMatrix[i][j]){
                Ik = i;
                Jk = j;
                break;
            }
        }
    } 
    //console.log('pos: '+boardMatrix[Ik][Jk]); 
    var leftk = Jk;
    var rightk = Jk;
    var upk = Ik;
    var downk = Ik;

    var nwleftk = Jk;
    var nwupk = Ik;
    var nerightk = Jk;
    var neupk = Ik;
    var serightk = Jk;
    var sedownk = Ik;
    var swleftk = Jk;
    var swdownk = Ik;

    var leftsk = document.getElementById(boardMatrix[Ik][Jk]);
    var rightsk = document.getElementById(boardMatrix[Ik][Jk]);
    var upsk = document.getElementById(boardMatrix[Ik][Jk]);
    var downsk = document.getElementById(boardMatrix[Ik][Jk]);

    var nwk = document.getElementById(boardMatrix[Ik][Jk]);
    var nek = document.getElementById(boardMatrix[Ik][Jk]);  
    var swk = document.getElementById(boardMatrix[Ik][Jk]);
    var sek = document.getElementById(boardMatrix[Ik][Jk]);


    var pawntrk = '';
    var pawntlk = '';
    var typeFound = '';
    var piecesFoundc = [];
      
     //initialises objects each time
    function movable(){
        var rstart = false;
        var lstart = false;
        var ustart = false;
        var dstart = false;

        var nwstart = false;
        var nestart = false;
        var swstart = false;
        var sestart = false;
        for(var i=0; i<8; i++){

        if(theType=='rook'&&checkColour==oppColour||theType=='queen'&&checkColour==oppColour){   
            if(rightk<8){
                rightsk = document.getElementById(boardMatrix[Ik][rightk]);
            }if(leftk>-1){
                leftsk = document.getElementById(boardMatrix[Ik][leftk]);
            }if(upk<8){
                upsk = document.getElementById(boardMatrix[upk][Jk]); 
            }if(downk>-1){
                downsk = document.getElementById(boardMatrix[downk][Jk]);
            }
                    
            if(rightk<8){
                if(rightsk!=null){
                    if(rightsk.id!=posId){
                        if(!rightsk.firstElementChild||!rstart){
                            rightk++;
                            rstart = true;
                        }
                    }
                }
            }
            if(leftk>-1){
                if(leftsk!=null){
                    if(leftsk.id!=posId){
                        if(!leftsk.firstElementChild||!lstart){
                            leftk--;
                            lstart = true;
                        }
                    }
                }
            }
            if(upk<8){
                if(upsk!=null){
                    if(upsk.id!=posId){
                        if(!upsk.firstElementChild||!ustart){
                            upk++;
                            ustart = true;
                        }
                    }
                }
            }

            if(downk>-1){
                if(downsk!=null){
                    if(downsk.id!=posId){
                        if(!downsk.firstElementChild||!dstart){
                            downk--;
                            dstart = true;
                        }
                    }
                }
            }
        }
        if(theType=='bishop'&&checkColour==oppColour||theType=='queen'&&checkColour==oppColour){
              
                if(nwleftk>-1&&nwupk<8){
                    nwk = document.getElementById(boardMatrix[nwupk][nwleftk]);
                    nwArrk.push(nwk);
                }if(nerightk<8&&neupk<8){
                    nek = document.getElementById(boardMatrix[neupk][nerightk]);
                    neArrk.push(nek);
                }if(swleftk>-1&&swdownk>-1){
                    swk = document.getElementById(boardMatrix[swdownk][swleftk]);
                    swArrk.push(swk);
                }if(serightk<8&&sedownk>-1){
                    sek = document.getElementById(boardMatrix[sedownk][serightk]);
                    seArrk.push(sek);
                }         

                
                if(nwleftk>-1&&nwupk<8){
                    if(nwk!=null){
                        if(nwk.id!=posId){
                            if(!nwk.firstElementChild||!nwstart){
                                nwleftk--;
                                nwupk++;
                                nwstart = true;
                            }
                        }     
                    }
                }
                if(nerightk<8&&neupk<8){
                    if(nek!=null){
                        if(nek.id!=posId){
                            if(!nek.firstElementChild||!nestart){
                                nerightk++;
                                neupk++;
                                nestart = true;
                            }
                        }
                    }
                }
                if(swleftk>-1&&swdownk>-1){
                    if(swk!=null){
                        if(swk.id!=posId){
                            if(!swk.firstElementChild||!swstart){
                                swleftk--;
                                swdownk--;
                                swstart = true;
                            }
                        }
                    }
                }
                if(serightk<8&&sedownk>-1){
                    if(sek!=null){
                        if(sek.id!=posId){
                            if(!sek.firstElementChild||!sestart){
                                serightk++;
                                sedownk--;
                                sestart = true;
                            }
                        } 
                    }
                }
            }         
        }     
    }
    movable();
    //console.log('hey: '+downk);
    if(rightsk!=null){
        var val = rightsk;
        var valId = rightsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    }

    if(leftsk!=null){
        var val = leftsk;
        var valId = leftsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 

    if(upsk!=null){
        var val = upsk;
        var valId = upsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        }
    } 

    if(downsk!=null){
        var val = downsk;
        var valId = downsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 
    if(nwk!=null){
        var val = nwk;
        var valId = nwk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 

    if(nek!=null){
        var val = nek;
        var valId = nek.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        }       
    } 

    if(swk!=null){
        var val = swk;
        var valId = swk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 

    if(sek!=null){
        var val = sek;
        var valId = sek.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 
    
    var p = pawnCanCheck(Ik, Jk, theType, posId, checkColour);
    if(p!=''){
        piecesFoundc = p;
    }

    if(theType=='horse'&&checkColour==oppColour){
        
        if([Ik+2]<8&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik+2][Jk-1]);
        }
        if([Ik+2]<8&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik+2][Jk+1]);
        }
        if([Ik+1]<8&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik+1][Jk+2]);
        }
        if([Ik-1]>-1&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik-1][Jk+2]);
        }
        if([Ik-2]>-1&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik-2][Jk+1]);
        }
        if([Ik-2]>-1&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik-2][Jk-1]);
        }
        if([Ik+1]<8&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik+1][Jk-2]);
        }
        if([Ik-1]>-1&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik-1][Jk-2]);
        }
    }

    for(var t=0; t<horseArrk.length; t++){
        var valId = horseArrk[t];
        if(valId==posId){
            piecesFoundc = valId;
        }
    }
    //console.log('hello pos: '+posId+' piecesFoundc: '+piecesFoundc);
    if(piecesFoundc==posId){
        //console.log('HOORAY');
        return true;
    }else{
        //console.log('piecesFoundc: '+piecesFoundc);
        return false;
    }

}

function canSave(controlId, posId){
    var control = document.getElementById(controlId);
    var theType = control.classList[1];
    var checkColour = control.classList[0];
    var thePlaceId = control.parentNode.id;
    //console.log('attcking piece: '+thePlaceId);
    //console.log('checker type: '+theType+' checkColour: '+checkColour+' id: '+controlId+' colour '+colour);
    var horseArrk = [];
    var kingsArrayk = [];
    var nwArrk = [];
    var neArrk = [];
    var swArrk = [];
    var seArrk = [];
    var Ik = 0;
    var Jk = 0;

    for(var i=0; i<8; i++){
        for(var j=0; j<8; j++){
            if(thePlaceId==boardMatrix[i][j]){
                Ik = i;
                Jk = j;
                break;
            }
        }
    } 
    //console.log('pos: '+boardMatrix[Ik][Jk]); 
    var leftk = Jk;
    var rightk = Jk;
    var upk = Ik;
    var downk = Ik;

    var nwleftk = Jk;
    var nwupk = Ik;
    var nerightk = Jk;
    var neupk = Ik;
    var serightk = Jk;
    var sedownk = Ik;
    var swleftk = Jk;
    var swdownk = Ik;

    var leftsk = document.getElementById(boardMatrix[Ik][Jk]);
    var rightsk = document.getElementById(boardMatrix[Ik][Jk]);
    var upsk = document.getElementById(boardMatrix[Ik][Jk]);
    var downsk = document.getElementById(boardMatrix[Ik][Jk]);

    var nwk = document.getElementById(boardMatrix[Ik][Jk]);
    var nek = document.getElementById(boardMatrix[Ik][Jk]);  
    var swk = document.getElementById(boardMatrix[Ik][Jk]);
    var sek = document.getElementById(boardMatrix[Ik][Jk]);


    var pawntrk = '';
    var pawntlk = '';
    var typeFound = '';
    var piecesFoundc = [];
      
     //initialises objects each time
    function movable(){
        var rstart = false;
        var lstart = false;
        var ustart = false;
        var dstart = false;

        var nwstart = false;
        var nestart = false;
        var swstart = false;
        var sestart = false;
        for(var i=0; i<8; i++){
        //console.log("type: "+theType+' checkcolour: '+checkColour+' posId: '+posId);
        if(theType=='rook'&&checkColour==setColour||theType=='queen'&&checkColour==setColour){   
            if(rightk>-1){
                rightsk = document.getElementById(boardMatrix[Ik][rightk]); 
            }if(leftk<8){
                leftsk = document.getElementById(boardMatrix[Ik][leftk]);  
            }if(upk>-1){
                upsk = document.getElementById(boardMatrix[upk][Jk]); 
            }if(downk<8){
                downsk = document.getElementById(boardMatrix[downk][Jk]);
            }       
                    
           
            if(rightk<8&&rightk>-1){
                if(rightsk!=null){
                    if(rightsk.id!=posId){
                        if(!rightsk.firstElementChild||!rstart){
                            rightk--;
                            rstart = true;
                        }
                    }
                }
            }   
            if(leftk>-1&&leftk<8){
                if(leftsk!=null){
                    if(leftsk.id!=posId){
                        if(!leftsk.firstElementChild||!lstart){
                            leftk++;
                            lstart = true;
                        }
                    }
                }
            }
            if(upk<8&&upk>-1){
                if(upsk!=null){
                    if(upsk.id!=posId){
                        if(!upsk.firstElementChild||!ustart){
                            upk--;
                            //console.log('hello up: '+up+' - '+ups);
                            ustart = true;
                        }
                    }
                }
            }
            if(downk>-1&&downk<8){
                if(downsk!=null){
                    if(downsk.id!=posId){
                        if(!downsk.firstElementChild||!dstart){
                            downk++;
                            dstart = true;
                        }
                    }
                }
            }
        }
   

        if(theType=='bishop'&&checkColour==setColour||theType=='queen'&&checkColour==setColour){
              
                if(nwleftk<8&&nwupk>-1){
                    nwk = document.getElementById(boardMatrix[nwupk][nwleftk]);
                    nwArrk.push(nwk);          
                }if(nerightk>-1&&neupk>-1){
                    nek = document.getElementById(boardMatrix[neupk][nerightk]);
                    neArrk.push(nek);     
                }if(swleftk<8&&swdownk<8){
                    swk = document.getElementById(boardMatrix[swdownk][swleftk]);
                    swArrk.push(swk);
                }if(serightk>-1&&sedownk<8){
                    sek = document.getElementById(boardMatrix[sedownk][serightk]);
                    seArrk.push(sek);  
                }
                
                if(nwleftk<8&&nwupk>-1){
                    if(nwk!=null){
                        if(nwk.id!=posId){
                            if(!nwk.firstElementChild||!nwstart){
                                nwleftk++;
                                nwupk--;
                                nwstart = true;
                            }
                        }     
                    }
                }
                if(nerightk>-1&&neupk>-1){
                    if(nek!=null){
                        if(nek.id!=posId){
                            if(!nek.firstElementChild||!nestart){
                                nerightk--;
                                neupk--;
                                nestart = true;
                            }
                        }
                    }
                }
                if(swleftk<8&&swdownk<8){
                    if(swk!=null){
                        if(swk.id!=posId){
                            if(!swk.firstElementChild||!swstart){
                                swleftk++;
                                swdownk++;
                                swstart = true;
                            }
                        }
                    }
                }
                if(serightk>-1&&sedownk<8){
                    if(sek!=null){
                        if(sek.id!=posId){
                            if(!sek.firstElementChild||!sestart){
                                serightk--;
                                sedownk++;
                                sestart = true;
                            }
                        } 
                    }
                }
            }         
        }     
    }
    movable();
    //console.log('hey: '+downk);
    if(rightsk!=null){
        var val = rightsk;
        var valId = rightsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    }

    if(leftsk!=null){
        var val = leftsk;
        var valId = leftsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 

    if(upsk!=null){
        var val = upsk;
        var valId = upsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        }
    } 

    if(downsk!=null){
        var val = downsk;
        var valId = downsk.id;
        //console.log("currDir down: "+valId+" - "+posId);
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 
    if(nwk!=null){
        var val = nwk;
        var valId = nwk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 

    if(nek!=null){
        var val = nek;
        var valId = nek.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        }       
    } 

    if(swk!=null){
        var val = swk;
        var valId = swk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
                //console.log("valid: "+valId+" pf: "+piecesFoundc)
            }
        } 
    } 

    if(sek!=null){
        var val = sek;
        var valId = sek.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 
    //console.log("canSave");
    var p = pawnCanSave(Ik, Jk, theType, posId, checkColour);
    if(p!=''){
        piecesFoundc = p;
    }

    //console.log("controlId: "+controlId+' type: '+theType);
    if(theType=='horse'&&checkColour==setColour){
        
        if([Ik+2]<8&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik+2][Jk-1]);
        }
        if([Ik+2]<8&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik+2][Jk+1]);
        }
        if([Ik+1]<8&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik+1][Jk+2]);
        }
        if([Ik-1]>-1&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik-1][Jk+2]);
        }
        if([Ik-2]>-1&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik-2][Jk+1]);
        }
        if([Ik-2]>-1&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik-2][Jk-1]);
        }
        if([Ik+1]<8&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik+1][Jk-2]);
        }
        if([Ik-1]>-1&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik-1][Jk-2]);
        }
    }

    for(var t=0; t<horseArrk.length; t++){
        var valId = horseArrk[t];
        if(valId==posId){
            piecesFoundc = valId;
            //console.log("found: "+piecesFoundc);
        }
    }
    //console.log('hello pos: '+posId+' piecesFoundc: '+piecesFoundc);
    if(piecesFoundc==posId){
        //console.log('HOORAY');
        return true;
    }else{
        //console.log('piecesFoundc: '+piecesFoundc);
        return false;
    }

}

function canGet(controlId, posId){
    var control = document.getElementById(controlId);
    var theType = control.classList[1];
    var checkColour = control.classList[0];
    var thePlaceId = control.parentNode.id;
    //console.log('attcking piece: '+thePlaceId);
    //console.log('checker type: '+theType+' checkColour: '+checkColour+' id: '+controlId+' colour '+colour);
    var horseArrk = [];
    var kingsArrayk = [];
    var nwArrk = [];
    var neArrk = [];
    var swArrk = [];
    var seArrk = [];
    var Ik = 0;
    var Jk = 0;

    for(var i=0; i<8; i++){
        for(var j=0; j<8; j++){
            if(thePlaceId==boardMatrix[i][j]){
                Ik = i;
                Jk = j;
                break;
            }
        }
    } 
    //console.log('pos: '+boardMatrix[Ik][Jk]); 
    var leftk = Jk;
    var rightk = Jk;
    var upk = Ik;
    var downk = Ik;

    var nwleftk = Jk;
    var nwupk = Ik;
    var nerightk = Jk;
    var neupk = Ik;
    var serightk = Jk;
    var sedownk = Ik;
    var swleftk = Jk;
    var swdownk = Ik;

    var leftsk = document.getElementById(boardMatrix[Ik][Jk]);
    var rightsk = document.getElementById(boardMatrix[Ik][Jk]);
    var upsk = document.getElementById(boardMatrix[Ik][Jk]);
    var downsk = document.getElementById(boardMatrix[Ik][Jk]);

    var nwk = document.getElementById(boardMatrix[Ik][Jk]);
    var nek = document.getElementById(boardMatrix[Ik][Jk]);  
    var swk = document.getElementById(boardMatrix[Ik][Jk]);
    var sek = document.getElementById(boardMatrix[Ik][Jk]);


    var pawntrk = '';
    var pawntlk = '';
    var typeFound = '';
    var piecesFoundc = [];
      
     //initialises objects each time
    function movable(){
        var rstart = false;
        var lstart = false;
        var ustart = false;
        var dstart = false;

        var nwstart = false;
        var nestart = false;
        var swstart = false;
        var sestart = false;
        for(var i=0; i<8; i++){

        if(theType=='rook'&&checkColour==setColour||theType=='queen'&&checkColour==setColour){   
            if(rightk>-1){
                rightsk = document.getElementById(boardMatrix[Ik][rightk]); 
            }if(leftk<8){
                leftsk = document.getElementById(boardMatrix[Ik][leftk]);  
            }if(upk>-1){
                upsk = document.getElementById(boardMatrix[upk][Jk]); 
            }if(downk<8){
                downsk = document.getElementById(boardMatrix[downk][Jk]);
            }       
                    
           
            if(rightk<8&&rightk>-1){
                if(rightsk!=null){
                    if(rightsk.id!=posId){
                        if(!rightsk.firstElementChild||!rstart){
                            rightk--;
                            rstart = true;
                        }
                    }
                }
            }   
            if(leftk>-1&&leftk<8){
                if(leftsk!=null){
                    if(leftsk.id!=posId){
                        if(!leftsk.firstElementChild||!lstart){
                            leftk++;
                            lstart = true;
                        }
                    }
                }
            }
            if(upk<8&&upk>-1){
                if(upsk!=null){
                    if(upsk.id!=posId){
                        if(!upsk.firstElementChild||!ustart){
                            upk--;
                            //console.log('hello up: '+up+' - '+ups);
                            ustart = true;
                        }
                    }
                }
            }
            if(downk>-1&&downk<8){
                if(downsk!=null){
                    if(downsk.id!=posId){
                        if(!downsk.firstElementChild||!dstart){
                            downk++;
                            dstart = true;
                        }
                    }
                }
            }
        }
        if(theType=='bishop'&&checkColour==setColour||theType=='queen'&&checkColour==setColour){
              
                if(nwleftk<8&&nwupk>-1){
                    nwk = document.getElementById(boardMatrix[nwupk][nwleftk]);
                    nwArrk.push(nwk);          
                }if(nerightk>-1&&neupk>-1){
                    nek = document.getElementById(boardMatrix[neupk][nerightk]);
                    neArrk.push(nek);     
                }if(swleftk<8&&swdownk<8){
                    swk = document.getElementById(boardMatrix[swdownk][swleftk]);
                    swArrk.push(swk);
                }if(serightk>-1&&sedownk<8){
                    sek = document.getElementById(boardMatrix[sedownk][serightk]);
                    seArrk.push(sek);  
                }
                
                if(nwleftk<8&&nwupk>-1){
                    if(nwk!=null){
                        if(nwk.id!=posId){
                            if(!nwk.firstElementChild||!nwstart){
                                nwleftk++;
                                nwupk--;
                                nwstart = true;
                            }
                        }     
                    }
                }
                if(nerightk>-1&&neupk>-1){
                    if(nek!=null){
                        if(nek.id!=posId){
                            if(!nek.firstElementChild||!nestart){
                                nerightk--;
                                neupk--;
                                nestart = true;
                            }
                        }
                    }
                }
                if(swleftk<8&&swdownk<8){
                    if(swk!=null){
                        if(swk.id!=posId){
                            if(!swk.firstElementChild||!swstart){
                                swleftk++;
                                swdownk++;
                                swstart = true;
                            }
                        }
                    }
                }
                if(serightk>-1&&sedownk<8){
                    if(sek!=null){
                        if(sek.id!=posId){
                            if(!sek.firstElementChild||!sestart){
                                serightk--;
                                sedownk++;
                                sestart = true;
                            }
                        } 
                    }
                }
            }         
        }     
    }
    movable();
    //console.log('hey: '+downk);
    if(rightsk!=null){
        var val = rightsk;
        var valId = rightsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    }

    if(leftsk!=null){
        var val = leftsk;
        var valId = leftsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 

    if(upsk!=null){
        var val = upsk;
        var valId = upsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        }
    } 

    if(downsk!=null){
        var val = downsk;
        var valId = downsk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 
    if(nwk!=null){
        var val = nwk;
        var valId = nwk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 

    if(nek!=null){
        var val = nek;
        var valId = nek.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        }       
    } 

    if(swk!=null){
        var val = swk;
        var valId = swk.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 

    if(sek!=null){
        var val = sek;
        var valId = sek.id;
        if(val!=null){
            if(valId==posId){
                piecesFoundc = valId;
            }
        } 
    } 
    
    var p = pawnCanGet(Ik, Jk, theType, posId, checkColour);
    if(p!=''){
        piecesFoundc = p;
    }
    
    if(theType=='horse'&&checkColour==setColour){
        
        if([Ik+2]<8&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik+2][Jk-1]);
        }
        if([Ik+2]<8&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik+2][Jk+1]);
        }
        if([Ik+1]<8&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik+1][Jk+2]);
        }
        if([Ik-1]>-1&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik-1][Jk+2]);
        }
        if([Ik-2]>-1&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik-2][Jk+1]);
        }
        if([Ik-2]>-1&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik-2][Jk-1]);
        }
        if([Ik+1]<8&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik+1][Jk-2]);
        }
        if([Ik-1]>-1&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik-1][Jk-2]);
        }
    }

    for(var t=0; t<horseArrk.length; t++){
        var valId = horseArrk[t];
        if(valId==posId){
            piecesFoundc = valId;
        }
    }
    //console.log('hello pos: '+posId+' piecesFoundc: '+piecesFoundc);
    if(piecesFoundc==posId){
        //console.log('HOORAY');
        return true;
    }else{
        //console.log('piecesFoundc: '+piecesFoundc);
        return false;
    }

}

function pawnCanSave(i, j, ptype, ppos, pccolour){
    //console.log("in pawncansave: "+ptype+' '+pccolour+' '+colour);
    var pieceFound = '';
    if(ptype=='pawn'&&pccolour==setColour){
        //console.log("in p save");
        var ispfront = false;
        var ispfront2 = false;
        if(i-1>-1){
            var valId = boardMatrix[i-1][j]; 
            var val = document.getElementById(valId);
            //console.log("in pawncansave");
            if(val.hasChildNodes()){
                ispfront = true;
            }
            if(valId==ppos&&!ispfront){
                pieceFound = valId;
            }        
        }
        if(!ispfront){
            if(i-2>-1){
                var valId = boardMatrix[i-2][j];
                var val = document.getElementById(valId);
                if(val.hasChildNodes()){
                    ispfront2 = true;
                } 
                var mypawnId = boardMatrix[i][j];
                //console.log("mypawn id: "+mypawnId);
                var mypawnplace = document.getElementById(boardMatrix[i][j]);
                var mypawn = mypawnplace.firstElementChild.id;
                //console.log("mypawn: "+mypawn);
                var uniqPawn2 = false; 
                if(valId==ppos&&!ispfront2){
                    var m = 0;
                    for(m=0; m<pawnIdArr.length; m++){
                        if(mypawn==pawnIdArr[m]){
                            break;
                        }
                    }

                    if(m==pawnIdArr.length){
                        uniqPawn2 = true;
                    }else{
                        uniqPawn2 = false;
                    }

                    if(uniqPawn2){
                        pieceFound = valId;    
                    }
                }             
            }
        }
    }
    return pieceFound;
}

function pawnCanGet(i, j, ptype, ppos, pccolour){
    var pieceFound = '';
    if(ptype=='pawn'&&pccolour==setColour){
        var ispright = false;
        var ispleft = false;
        if(i-1>-1&&j-1>-1){
            var valId = boardMatrix[i-1][j-1];
            var val = document.getElementById(valId);
            if(val.hasChildNodes()){
                ispright = true;
            }
            if(valId==ppos&&ispright){
                pieceFound = valId;
            }     
        }
        if(i-1>-1&&j+1<8){
            var valId = boardMatrix[i-1][j+1]; 
            var val = document.getElementById(valId);
              if(val.hasChildNodes()){
                ispleft = true;
            }
            if(valId==ppos&&ispleft){
                pieceFound = valId;
            }        
        }
    }
    return pieceFound;
}

function pawnCanCheck(i, j, ptype, ppos, pccolour){
    var pieceFound = '';
    if(ptype=='pawn'&&pccolour==oppColour){
        var ispright = false;
        var ispleft = false;
        if(i+1<8&&j-1>-1){
            var valId = boardMatrix[i+1][j-1];
            var val = document.getElementById(valId);
            if(val.hasChildNodes()){
                ispright = true;
            }
            if(valId==ppos&&ispright){
                pieceFound = valId;
            }     
        }
        if(i+1<8&&j+1<8){
            var valId = boardMatrix[i+1][j+1]; 
            var val = document.getElementById(valId);
              if(val.hasChildNodes()){
                ispleft = true;
            }
            if(valId==ppos&&ispleft){
                pieceFound = valId;
            }        
        }
    }
    return pieceFound;
}
function kingCanCheck(controlId, posId){
    var control = document.getElementById(controlId);
    var theType = control.classList[1];
    var checkColour = control.classList[0];
    var thePlaceId = control.parentNode.id;
    var poss = document.getElementById(posId); 
    kingPiece = poss.firstElementChild;
    kingCol = kingPiece.classList[0];
    //console.log('checker type: '+theType+' checkColour: '+checkColour+' id: '+controlId+' colour '+colour);
    var horseArrk = [];
    var kingsArrayk = [];
    var nwArrk = [];
    var neArrk = [];
    var swArrk = [];
    var seArrk = [];
    var Ik = 0;
    var Jk = 0;

    guardAttack = '';

    for(var i=0; i<8; i++){
        for(var j=0; j<8; j++){
            if(thePlaceId==boardMatrix[i][j]){
                Ik = i;
                Jk = j;
                break;
            }
        }
    } 
    //console.log('pos: '+boardMatrix[Ik][Jk]); 
    var leftk = Jk;
    var rightk = Jk;
    var upk = Ik;
    var downk = Ik;


    
    
    var nwleftk = Jk;
    var nwupk = Ik;
    var nerightk = Jk;
    var neupk = Ik;
    var serightk = Jk;
    var sedownk = Ik;
    var swleftk = Jk;
    var swdownk = Ik;


    
    var isNwCh = false; 
    var isNeCh = false;
    var isSwCh = false;          
    var isSeCh = false;
    var isNwCh2 = false; 
    var isNeCh2 = false;     
    var isSwCh2 = false;
    var isSeCh2 = false;

    var leftsk = document.getElementById(boardMatrix[Ik][Jk]);
    var rightsk = document.getElementById(boardMatrix[Ik][Jk]);
    var upsk = document.getElementById(boardMatrix[Ik][Jk]);
    var downsk = document.getElementById(boardMatrix[Ik][Jk]);

    var nwk = document.getElementById(boardMatrix[Ik][Jk]);
    var nek = document.getElementById(boardMatrix[Ik][Jk]);  
    var swk = document.getElementById(boardMatrix[Ik][Jk]);
    var sek = document.getElementById(boardMatrix[Ik][Jk]);


    var pawntrk = '';
    var pawntlk = '';
    var typeFound = '';
    var piecesFoundc = [];
      
     //initialises objects each time
    function movable(){
        var rstart = false;
        var lstart = false;
        var ustart = false;
        var dstart = false;


        var nwstart = false;
        var nestart = false;
        var swstart = false;
        var sestart = false;
        for(var i=0; i<8; i++){

        if(theType=='rook'&&checkColour==oppColour||theType=='queen'&&checkColour==oppColour){   
            if(rightk<8){
                rightsk = document.getElementById(boardMatrix[Ik][rightk]);
            }if(leftk>-1){
                leftsk = document.getElementById(boardMatrix[Ik][leftk]);
            }if(upk<8){
                upsk = document.getElementById(boardMatrix[upk][Jk]); 
            }if(downk>-1){
                downsk = document.getElementById(boardMatrix[downk][Jk]);
            }
                    
                    
            if(rightk<8){
                if(rightsk!=null){
                    var ropp = true;
                    if(rightsk.id!=posId){
                        ropp = false;
                    }
                    if(!rightsk.firstElementChild||!rstart||!ropp){
                        rightk++;
                        rstart = true;
                        ropp = true;
                    }
                }
            }
            if(leftk>-1){
                if(leftsk!=null){
                    var lopp = true;
                    if(leftsk.id!=posId){
                        lopp = false;    
                    }
                    if(!leftsk.firstElementChild||!lstart||!lopp){
                        leftk--;
                        lstart = true;
                        lopp = true;
                    }
                }
            }
            if(upk<8){
                if(upsk!=null){
                    var uopp = true;
                    if(upsk.id!=posId){
                        uopp = false;
                    }
                    if(!upsk.firstElementChild||!ustart||!uopp){
                        upk++;
                        ustart = true;
                        uopp = true;
                    }
                }
            }

            if(downk>-1){
                if(downsk!=null){
                    var dopp = true;
                    if(downsk.id!=posId){
                        dopp = false;    
                    }
                    if(!downsk.firstElementChild||!dstart||!dopp){
                        downk--;
                        dstart = true;
                        dopp = true;
                    }
                }
            }
        }
        if(theType=='bishop'&&checkColour==oppColour||theType=='queen'&&checkColour==oppColour){
              
                if(nwleftk>-1&&nwupk<8){
                    nwk = document.getElementById(boardMatrix[nwupk][nwleftk]);
                    //console.log("nw can check: "+nwk.id);
                    nwArrk.push(nwk);
                }if(nerightk<8&&neupk<8){
                    nek = document.getElementById(boardMatrix[neupk][nerightk]);
                    neArrk.push(nek);
                    //console.log("kccheck: "+nek.id);
                }if(swleftk>-1&&swdownk>-1){
                    swk = document.getElementById(boardMatrix[swdownk][swleftk]);
                    swArrk.push(swk);
                }if(serightk<8&&sedownk>-1){
                    sek = document.getElementById(boardMatrix[sedownk][serightk]);
                    seArrk.push(sek);
                }  
                
                if(nwleftk>-1&&nwupk<8){
                    if(nwk!=null){
                        var nwopp = true;
                        if(nwk.id!=posId){
                            nwopp = false;
                        }
                        //console.log("nw inc: "+!nwk.firstElementChild+" - "+!nwstart+" - "+!nwopp);
                        if(!nwk.firstElementChild||!nwstart||!nwopp){
                            nwleftk--;
                            nwupk++;
                            nwstart = true;
                            nwopp = true;
                        }
                    }
                }
                if(nerightk<8&&neupk<8){
                    if(nek!=null){
                        var neopp = true;
                        if(nek.id!=posId){
                            neopp = false;        
                        }
                        if(!nek.firstElementChild||!nestart||!neopp){
                            nerightk++;
                            neupk++;
                            nestart = true;
                            neopp = true;
                        }
                    }
                }
                if(swleftk>-1&&swdownk>-1){
                    if(swk!=null){
                        var swopp = true;
                        if(swk.id!=posId){
                            //console.log('hi swopp false');
                            swopp = false;
                        }
                        if(!swk.firstElementChild||!swstart||!swopp){
                            swleftk--;
                            swdownk--;
                            swstart = true;
                            swopp = true;
                        }
                    }
                }
                if(serightk<8&&sedownk<-1){
                    if(sek!=null){
                        var seopp = true;
                        if(sek.id!=posId){
                            seopp = false;
                        }
                        if(!sek.firstElementChild||!sestart||!seopp){
                            serightk++;
                            sedownk--;
                            sestart = true;
                            seopp = true;
                        } 
                    }
                }
            }         
        }     
    }
    movable();
    //console.log('hey: '+downk);
    if(rightsk!=null){
        //if(rightsk.hasChildNodes()){
            var val = rightsk;
            var valId = rightsk.id;
            //console.log('r posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi r '+val.id);
                if(valId==posId){
                    piecesFoundc = valId;
                    dirSec = 'right';
                    guardAttack = thePlaceId;
                    //console.log('r: '+rightsk.id);

                }
            }
        //} 
    }
    if(leftsk!=null){
        //if(leftsk.hasChildNodes()){
            var val = leftsk;
            var valId = leftsk.id;
            //console.log('l posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi l '+val.classList[1]);
                if(valId==posId){
                    piecesFoundc = valId;
                    dirSec = 'left';
                    guardAttack = thePlaceId;
                    //console.log('l: '+leftsk.id);
                }
            } 
        //}
    } 

    if(upsk!=null){
        //if(upsk.hasChildNodes()){
            var val = upsk;
            var valId = upsk.id;
            //console.log('up posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi u '+val.classList[1]);
                if(valId==posId){
                    piecesFoundc = valId;
                    dirSec = 'up';
                    guardAttack = thePlaceId;
                    //console.log('u: '+upsk.id);
                }
            } 
        //}
    } 

    if(downsk!=null){
        //if(downsk.hasChildNodes()){
            var val = downsk;
            var valId = downsk.id;
            //console.log('d posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi d '+val.classList[1]);
                if(valId==posId){
                    piecesFoundc = valId;
                    dirSec = 'down';
                    guardAttack = thePlaceId;
                    //console.log('d: '+downsk.id);
                }
            } 
        //}
    } 
    if(nwk!=null){
        //if(nwk.hasChildNodes()){
            var val = nwk;
            var valId = nwk.id;
            //console.log('nw posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log("val: "+valId+" - "+posId);
                if(valId==posId){
                    piecesFoundc = valId;
                    dirSec = 'nw';
                    guardAttack = thePlaceId;
                    //console.log('nw: '+nwk.id);
                }
            } 
        //}
    } 

    if(nek!=null){
        //if(nek.hasChildNodes()){
            var val = nek;
            var valId = nek.id;
            //console.log('ne posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi ne '+val.classList[1]+' ne colour: '+val.classList[0]);
                if(valId==posId){
                    piecesFoundc = valId;
                    dirSec = 'ne';
                    guardAttack = thePlaceId;
                    //console.log('ne: '+nek.id);
                }
            } 
        //}       
    } 

    if(swk!=null){
        //if(swk.hasChildNodes()){
            var val = swk;
            var valId = swk.id;
            //console.log('sw posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi sw '+val.classList[1]);
                if(valId==posId){
                    piecesFoundc = valId;
                    dirSec = 'sw';
                    guardAttack = thePlaceId;
                }
            } 
        //}
    } 

    if(sek!=null){
        //if(sek.hasChildNodes()){
            var val = sek;
            var valId = sek.id;
            //console.log('se posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi se '+val.classList[1]+' ne colour: '+val.classList[0]+' colour: '+colour);
                if(valId==posId){
                    piecesFoundc = valId;
                    dirSec = 'se';
                    guardAttack = thePlaceId;
                    //console.log('se: '+sek.id);
                }
            } 
        //}
    }   

    if(theType=='pawn'&&checkColour!=colour){
        if(Ik+1<8&&Jk+1<8){
            var valId = boardMatrix[Ik+1][Jk+1];
            if(valId==posId){
                piecesFoundc = valId;
                guardAttack = thePlaceId;
                //attacker = thePlaceId;
            }     
        }
        if(Ik+1<8&&Jk-1>-1){
        var valId = boardMatrix[Ik+1][Jk-1];
            if(valId==posId){
                piecesFoundc = valId;
                guardAttack = thePlaceId;
                //attacker = thePlaceId;
            }       
        }
    }

    if(theType=='horse'&&checkColour==oppColour){
        
        if([Ik+2]<8&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik+2][Jk-1]);
        }
        if([Ik+2]<8&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik+2][Jk+1]);
        }
        if([Ik+1]<8&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik+1][Jk+2]);
        }
        if([Ik-1]>-1&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik-1][Jk+2]);
        }
        if([Ik-2]>-1&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik-2][Jk+1]);
        }
        if([Ik-2]>-1&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik-2][Jk-1]);
        }
        if([Ik+1]<8&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik+1][Jk-2]);
        }
        if([Ik-1]>-1&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik-1][Jk-2]);
        }
    }

    for(var t=0; t<horseArrk.length; t++){
        //if(nextHorse.hasChildNodes()){
            var valId = horseArrk[t];
          //  if(val!=null){
            //    if(val!=null){
                    //console.log('hi h '+val.classList[1]);
                    //console.log('h posId: '+posId+' valId: '+valId);
                    if(valId==posId){
                        piecesFoundc = valId;
                        guardAttack = thePlaceId;
                    }
               // }
            //} 
       // }
    }
    //console.log('is: '+piecesFoundc);
    //console.log('guardAttack piece: '+guardAttack);
    if(piecesFoundc==posId){
        //console.log('HOORAY');
        return true;
    }else{
        return false;
    }

}

function finalCanCheck(controlId, posId){
    var control = document.getElementById(controlId);
    var theType = control.classList[1];
    var checkColour = control.classList[0];
    var thePlaceId = control.parentNode.id;
    currDir = [];

    //console.log('attcking piece: '+thePlaceId);
    //console.log('checker type: '+theType+' checkColour: '+checkColour+' id: '+controlId+' colour '+colour);
    var horseArrk = [];
    var kingsArrayk = [];
    var nwArrk = [];
    var neArrk = [];
    var swArrk = [];
    var seArrk = [];
    var Ik = 0;
    var Jk = 0;

    attacker = '';
    for(var i=0; i<8; i++){
        for(var j=0; j<8; j++){
            if(thePlaceId==boardMatrix[i][j]){
                Ik = i;
                Jk = j;
                break;
            }
        }
    } 
    //console.log('pos: '+boardMatrix[Ik][Jk]); 
    var leftk = Jk;
    var rightk = Jk;
    var upk = Ik;
    var downk = Ik;

    var leftsk = document.getElementById(boardMatrix[Ik][Jk]);
    var rightsk = document.getElementById(boardMatrix[Ik][Jk]);
    var upsk = document.getElementById(boardMatrix[Ik][Jk]);
    var downsk = document.getElementById(boardMatrix[Ik][Jk]);

    var nwk = document.getElementById(boardMatrix[Ik][Jk]);
    var nek = document.getElementById(boardMatrix[Ik][Jk]);  
    var swk = document.getElementById(boardMatrix[Ik][Jk]);
    var sek = document.getElementById(boardMatrix[Ik][Jk]);
    
    
    var nwleftk = Jk;
    var nwupk = Ik;
    var nerightk = Jk;
    var neupk = Ik;
    var serightk = Jk;
    var sedownk = Ik;
    var swleftk = Jk;
    var swdownk = Ik;


    var rArrk = [];
    var lArrk = [];
    var uArrk = [];
    var dArrk = [];

    var nwArk = [];
    var neArk = [];
    var swArk = [];
    var seArk = [];

    var pawntrk = '';
    var pawntlk = '';
    var typeFound = '';
    var piecesFoundc = '';
      
     //initialises objects each time
    function movable(){
        var rstart = false;
        var lstart = false;
        var ustart = false;
        var dstart = false;


        var nwstart = false;
        var nestart = false;
        var swstart = false;
        var sestart = false;  
        
        var le = boardMatrix[Ik][Jk];
        var ri = boardMatrix[Ik][Jk];
        var upp = boardMatrix[Ik][Jk];
        var dwn = boardMatrix[Ik][Jk];

        var nnw = boardMatrix[Ik][Jk];
        var nne = boardMatrix[Ik][Jk];
        var ssw = boardMatrix[Ik][Jk];
        var sse  = boardMatrix[Ik][Jk];
        for(var i=0; i<8; i++){

            if(theType=='rook'&&checkColour==oppColour||theType=='queen'&&checkColour==oppColour){  
            //console.log("right idd: "+rightsk.id); 
            if(rightk>-1&&rightk<8&&ri!=posId){
                ri = boardMatrix[Ik][rightk];
                rightsk = document.getElementById(boardMatrix[Ik][rightk]);
                rArrk.push(ri);
            }if(leftk<8&&leftk>-1&&le!=posId){
                le = boardMatrix[Ik][leftk];
                leftsk = document.getElementById(boardMatrix[Ik][leftk]);
                lArrk.push(le);
            }if(upk<8&&upk>-1&&upp!=posId){
                upp = boardMatrix[upk][Jk];
                upsk = document.getElementById(boardMatrix[upk][Jk]);
                uArrk.push(upp); 
            }if(downk<8&&downk>-1&&dwn!=posId){
                dwn = boardMatrix[downk][Jk];
                downsk = document.getElementById(boardMatrix[downk][Jk]);
                dArrk.push(dwn);
            }
                    
                    
                    
           
           if(rightk<8){
                if(rightsk!=null){
                    if(!rightsk.firstElementChild||!rstart){
                        if(rightsk.id!=posId){
                            rightk++;
                            rstart = true;
                        }
                    }
                }
            }
            if(leftk>-1){
                if(leftsk!=null){
                    if(!leftsk.firstElementChild||!lstart){
                        if(leftsk.id!=posId){
                            leftk--;
                            lstart = true;
                        }
                    }
                }
            }
            if(upk<8){
                if(upsk!=null){
                    if(!upsk.firstElementChild||!ustart){
                        if(upsk.id!=posId){
                            upk++;
                            ustart = true;
                        }
                    }
                }
            }

            if(downk>-1){
                if(downsk!=null){
                    if(!downsk.firstElementChild||!dstart){
                        if(downsk.id!=posId){
                            downk--;
                            dstart = true;
                        }
                    }
                }
            }
            }
        if(theType=='bishop'&&checkColour==oppColour||theType=='queen'&&checkColour==oppColour){
              
                if(nwleftk>-1&&nwupk<8&&nnw!=posId){
                    nnw = boardMatrix[nwupk][nwleftk];
                    nwArk.push(boardMatrix[nwupk][nwleftk]);
                    nwk = document.getElementById(boardMatrix[nwupk][nwleftk]);
                    nwArrk.push(nnw);
                }if(nerightk<8&&neupk<8&&nne!=posId){
                    nne = boardMatrix[neupk][nerightk];
                    neArk.push(boardMatrix[neupk][nerightk]);
                    nek = document.getElementById(boardMatrix[neupk][nerightk]);
                    neArrk.push(nne);
                }if(swleftk>-1&&swdownk>-1&&ssw!=posId){
                    ssw = boardMatrix[swdownk][swleftk];
                    swArk.push(boardMatrix[swdownk][swleftk]);
                    swk = document.getElementById(boardMatrix[swdownk][swleftk]);
                    swArrk.push(swk);
                }if(serightk<8&&sedownk>-1&&sse!=posId){
                    sse = boardMatrix[sedownk][serightk];
                    seArk.push(boardMatrix[sedownk][serightk]);
                    sek = document.getElementById(boardMatrix[sedownk][serightk]);
                    seArrk.push(sse);
                }         

                
                if(nwleftk>-1&&nwupk<8){
                    if(nwk!=null){
                        if(!nwk.firstElementChild||!nwstart){
                            if(nwk.id!=posId){
                                nwleftk--;
                                nwupk++;
                                nwstart = true;
                            }
                        }     
                    }
                }
                if(nerightk<8&&neupk<8){
                    if(nek!=null){
                        if(!nek.firstElementChild||!nestart){
                            if(nek.id!=posId){
                                nerightk++;
                                neupk++;
                                nestart = true;
                            }
                        }
                    }
                }
                if(swleftk>-1&&swdownk>-1){
                    if(swk!=null){
                        if(!swk.firstElementChild||!swstart){
                            if(swk.id!=posId){
                                swleftk--;
                                swdownk--;
                                swstart = true;
                            }
                        }
                    }
                }
                if(serightk<8&&sedownk>-1){
                    if(sek!=null){
                        if(!sek.firstElementChild||!sestart){
                            if(sek.id!=posId){
                                serightk++;
                                sedownk--;
                                sestart = true;
                            }
                        } 
                    }
                }
            }         
        }     
    }
    movable();
    //console.log('hey: '+downk);
    if(dirSec=='right'){
    if(rightsk!=null){
        //if(rightsk.hasChildNodes()){
            var val = rightsk;
            var valId = rightsk.id;
            //console.log('r posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi r '+val.id);
                if(val.hasChildNodes()){
                    piecesFoundc = valId;
                    currDir = rArrk;
                    currDir.shift();
                    //attacker = thePlaceId;
                    //console.log('r: '+rightsk.id);
                }
            }
        //} 
    }
    }
    if(dirSec=='left'){
    if(leftsk!=null){
        //if(leftsk.hasChildNodes()){
            var val = leftsk;
            var valId = leftsk.id;
            //console.log('l posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi l '+val.classList[1]);
                if(val.hasChildNodes()){
                    piecesFoundc = valId;
                    currDir = lArrk;
                    currDir.shift();
                    //attacker = thePlaceId;
                    //console.log('l: '+leftsk.id);
                }
            } 
        //}
    } 
    }
    if(dirSec=='up'){
    if(upsk!=null){
        //if(upsk.hasChildNodes()){
            var val = upsk;
            var valId = upsk.id;
            //console.log('up posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi u '+val.classList[1]);
                if(val.hasChildNodes()){
                    piecesFoundc = valId;
                    currDir = uArrk;
                    currDir.shift();
                    //attacker = thePlaceId;
                    //console.log('u: '+upsk.id);
                }
            } 
        //}
    } 
    }

    if(dirSec=='down'){
    if(downsk!=null){
        //if(downsk.hasChildNodes()){
            var val = downsk;
            var valId = downsk.id;
            //console.log('d posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi d '+val.classList[1]);
                if(val.hasChildNodes()){
                    piecesFoundc = valId;
                    currDir = dArrk;
                    currDir.shift();
                    //attacker = thePlaceId;
                    //console.log('d: '+downsk.id);
                }
            } 
        //}
    }
    }

    if(dirSec=='nw'){ 
    if(nwk!=null){
        //if(nwk.hasChildNodes()){
            var val = nwk;
            var valId = nwk.id;
            //console.log('nw posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi nw '+val.classList[1]);
                if(val.hasChildNodes()){
                    piecesFoundc = valId;
                    currDir = nwArk;
                    currDir.shift();
                    //attacker = thePlaceId;
                    //console.log('nw: '+nwk.id);
                }
            } 
        //}
    } 
    }

    if(dirSec=='ne'){
    if(nek!=null){
        //if(nek.hasChildNodes()){
            var val = nek;
            var valId = nek.id;
            //console.log('ne posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi ne '+val.classList[1]+' ne colour: '+val.classList[0]);
                if(val.hasChildNodes()){
                    piecesFoundc = valId;
                    currDir = neArk;
                    currDir.shift();
                    //attacker = thePlaceId;
                }
            } 
        //}       
    }
    } 

    if(dirSec=='sw'){
    if(swk!=null){
        //if(swk.hasChildNodes()){
            var val = swk;
            var valId = swk.id;
            //console.log('sw posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi sw '+val.classList[1]);
                if(val.hasChildNodes()){
                    piecesFoundc = valId;
                    currDir = swArk;
                    //console.log("swAr: "+swAr.length);
                    currDir.shift();
                    //attacker = thePlaceId;
                }
            } 
        //}
    } 
    }

    if(dirSec=='se'){
    if(sek!=null){
        //if(sek.hasChildNodes()){
            var val = sek;
            var valId = sek.id;
            //console.log('se posId: '+posId+' valId: '+valId);
            if(val!=null){
                //console.log('hi se '+val.classList[1]+' ne colour: '+val.classList[0]+' colour: '+colour);
                if(val.hasChildNodes()){
                    piecesFoundc = valId;
                    currDir = seArk;
                    currDir.shift();
                    //attacker = thePlaceId;
                    //console.log('se: '+sek.id);
                }
            } 
        //}
    } 
    }

    if(theType=='pawn'&&checkColour==oppColour){
        if(Ik+8<8&&Jk+1<8){
            var valId = boardMatrix[Ik+1][Jk+1];
            if(valId==posId){
                piecesFoundc = valId;
                //attacker = thePlaceId;
            }     
        }
        if(Ik+1<8&&Jk-1>-1){
        var valId = boardMatrix[Ik+1][Jk-1];
            if(valId==posId){
                piecesFoundc = valId;
                //attacker = thePlaceId;
            }       
        }
    }    


    if(theType=='horse'&&checkColour==oppColour){
        
        if([Ik+2]<8&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik+2][Jk-1]);
        }
        if([Ik+2]<8&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik+2][Jk+1]);
        }
        if([Ik+1]<8&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik+1][Jk+2]);
        }
        if([Ik-1]>-1&&[Jk+2]<8){
            horseArrk.push(boardMatrix[Ik-1][Jk+2]);
        }
        if([Ik-2]>-1&&[Jk+1]<8){
            horseArrk.push(boardMatrix[Ik-2][Jk+1]);
        }
        if([Ik-2]>-1&&[Jk-1]>-1){
            horseArrk.push(boardMatrix[Ik-2][Jk-1]);
        }
        if([Ik+1]<8&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik+1][Jk-2]);
        }
        if([Ik-1]>-1&&[Jk-2]>-1){
            horseArrk.push(boardMatrix[Ik-1][Jk-2]);
        }
    }

    for(var t=0; t<horseArrk.length; t++){
        var valId = horseArrk[t];
        if(valId==posId){
            piecesFoundc = valId;
            //attacker = thePlaceId;
        }
    }
    if(piecesFoundc==posId){
        return true;
    }else{
        latestVal = piecesFoundc;
        //console.log("latest val: "+latestVal);
        return false;
    }
}




this.castleMoveL = function(){
    var newVal = localStorage.getItem('hasChanged');
    if(newVal == 'Y'){
    kingMovement('bking');
    var therook = document.getElementById('brook1');
    var theking = document.getElementById('bking');
    var kingpl = document.getElementById('r8C');
    var rookpl = document.getElementById('r8D');
    //var emppl = document.getElementById('r1B');
    var first = false;
    var pieceArr = isChecked('r8C', castleleftArr1);
    for(var m=0; m<pieceArr.length; m++){
        first = canCheck(pieceArr[m], 'r8C');
        if(first){
            kingpl.style.background = 'orange';
            highlights.push(kingpl);
            break;
        }
    }
    var sec = false;
    var pieceArr = isChecked('r8D', castleleftArr2);
    for(var b=0; b<pieceArr.length; b++){
        sec = canCheck(pieceArr[b], 'r8D');
        if(sec){
            rookpl.style.background = 'orange';
            highlights.push(rookpl);
            break;
        }
    }
  
    if(!kingpl.hasChildNodes()&&!rookpl.hasChildNodes()&&!sec&&!first&&!inCheck&&!kingHasMoved&&!rook1HasMoved){
        kingpl.appendChild(theking);
        rookpl.appendChild(therook);
        localStorage.setItem('hasChanged','N');
    }
}
}


this.castleMoveR = function(){
    var newVal = localStorage.getItem('hasChanged');
    if(newVal == 'Y'){
    kingMovement('bking');
    var therook = document.getElementById('brook2');
    var theking = document.getElementById('bking');
    var kingpl = document.getElementById('r8G');
    var rookpl = document.getElementById('r8F');
    var first = false;
    var pieceArr = isChecked('r8G', castlerightArr1);
    for(var b=0; b<pieceArr.length; b++){
        first = canCheck(pieceArr[b], 'r8G');
        if(first){
            kingpl.style.background = 'orange';
            highlights.push(kingpl);
            break;
        }
    }
    var sec = false;
    var pieceArr = isChecked('r8F', castlerightArr2);
    for(var n=0; n<pieceArr.length; n++){
        sec = canCheck(pieceArr[n], 'r8F');
        if(sec){
            rookpl.style.background = 'orange';
            highlights.push(rookpl);
            break;
        }
    }
    if(!kingpl.hasChildNodes()&&!rookpl.hasChildNodes()&&!first&&!sec&&!inCheck&&!kingHasMoved&&!rook2HasMoved){
        kingpl.appendChild(theking);
        rookpl.appendChild(therook);
        localStorage.setItem('hasChanged','N');
    }
}
}


this.chooseNew = function(controlId){
    //console.log(controlId);
    if(controlId=='queenOp'){
        selected.classList.remove(type);
        selected.classList.add('queen');
        type = 'queen';
        //console.log('hi choose '+type+' '+selected.classList[1]);
    } if(controlId=='pawnOp'){
        selected.classList.remove(type);
        selected.classList.add('pawn');
        type = 'pawn';
        //console.log('hi choose '+type+' '+selected.classList[1]);
    } if(controlId=='rookOp'){
        selected.classList.remove(type);
        selected.classList.add('rook');
        type = 'rook';
        //console.log('hi choose '+type+' '+selected.classList[1]);
    } if(controlId=='horseOp'){
        selected.classList.remove(type);
        selected.classList.add('horse');
        type = 'horse';
        //console.log('hi choose '+type+' '+selected.classList[1]);
    } if(controlId=='bishopOp'){
        selected.classList.remove(type);
        selected.classList.add('bishop');
        type = 'bishop';
        //console.log('hi choose '+type+' '+selected.classList[1]);
    }

}

function getQueenId(){
    counter = 0;
    queen_id = "bqueen";
    var my_ids = document.querySelectorAll('*[id]:not([id=""])')
    for(var i=0; i<my_ids.length; i++){
        var next = my_ids[i].id;
        // console.log("next id: "+next);
        next = String(next);
        var res = next.substring(0, 6);
        if(res == "bqueen"){
            counter++;
        }  
        queen_id = "bqueen"+counter;
    }
    return queen_id;
}


this.moveTo = function(controlId){
    
    nwplc = document.getElementById(controlId);
   
    localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
    localStorage.setItem("KingHasMoved", localStorage.getItem("KingHasMoved"));
    localStorage.setItem("Rook1HasMoved", localStorage.getItem("Rook1HasMoved"));
    localStorage.setItem("Rook2HasMoved", localStorage.getItem("Rook2HasMoved"));
    if(!nwplc.hasChildNodes()){
    // console.log('in empty move to');
    var newVal = localStorage.getItem('hasChanged');
    //console.log('in moveto: '+newVal); 
    if(newVal == 'Y'){
    //console.log(" in move to ");
    var control = document.getElementById(controlId);
    //console.log('hello moveto selectedid: '+selected.id);
    var option = document.getElementById('option');
    //console.log('controlId: '+controlId);
    var mtCanChoose = false;
    var value = '';
    var Prev = document.getElementById(prev);
    var movePrev = undefined;
    //console.log('prev: '+prev);
    for(var f=0; f<allIdArr.length; f++){
        if(allIdArr[f]===controlId&&!control.hasChildNodes()){
            movePrev = Prev;
            allIdArr = [];
            break;
        }
    }
    
    if(type=='rook'&&freeMov||type=='queen'&&freeMov){
        for(var j=right; j<=left; j++){
            if(j<8&&j>-1){
                if(controlId==boardMatrix[I][j]){
                    control.appendChild(selected);
                    if(movePrev){
                        movePrev.innerHTML = '';
                    }
                    if(selected.id=='brook1'){
                        rook1HasMoved = true;
                        localStorage.setItem("Rook1HasMoved", "Y");
                    }
                      if(selected.id=='brook2'){
                        rook2HasMoved = true;
                        localStorage.setItem("Rook2HasMoved", "Y");
                    }
                    //console.log('selectedid: '+selected.id+' - '+rook1HasMoved);
                    localStorage.setItem('hasChanged','N');
                }
            }
        }
    
        for(var i=up; i<=down; i++){
            if(i<8&&i>-1){
                if(controlId==boardMatrix[i][J]){
                    control.appendChild(selected);
                    if(movePrev){
                        movePrev.innerHTML = '';
                    }
                    if(selected.id=='brook1'){
                        rook1HasMoved = true;
                        localStorage.setItem("Rook1HasMoved", "Y");
                    }
                    if(selected.id=='brook2'){
                        rook2HasMoved = true;
                        localStorage.setItem("Rook2HasMoved", "Y");
                    }
                    localStorage.setItem('hasChanged','N');
                }
            }
        }

    }
    if(type=='rook'&&!freeMov||type=='queen'&&!freeMov){
        for(var q=right; q<=left; q++){
            if(q<8&&q>-1){
                if(controlId==boardMatrix[I][q]){
                    for(var b=0; b<currDir.length; b++){
                        if(controlId==currDir[b]){
                            control.appendChild(selected);
                            if(movePrev){
                                movePrev.innerHTML = '';
                            }
                            if(selected.id=='brook1'){
                                rook1HasMoved = true;
                                localStorage.setItem("Rook1HasMoved", "N");
                            }
                            if(selected.id=='brook2'){
                                rook2HasMoved = true;
                                localStorage.setItem("Rook2HasMoved", "Y");
                            }
                            localStorage.setItem('hasChanged','N');
                        }
                    }
                }
            }
        }
    
        for(var r=up; r<=down; r++){
            if(r<8&&r>-1){
                if(controlId==boardMatrix[r][J]){
                    for(var c=0; c<currDir.length; c++){
                        if(controlId==currDir[c]){
                            control.appendChild(selected);
                            if(movePrev){
                                movePrev.innerHTML = '';
                            }
                            if(selected.id=='wrook1'){
                                rook1HasMoved = true;
                                localStorage.setItem("Rook1HasMoved", "Y");
                            }
                            if(selected.id=='wrook2'){
                                rook2HasMoved = true;
                                localStorage.setItem("Rook2HasMoved", "Y");
                            }
                            localStorage.setItem('hasChanged','N');
                        }
                    }
                }
            }
        }

    }

    if(type=='bishop'&&freeMov||type=='queen'&&freeMov){
        for(var p=0; p<fullArr.length; p++){
            if(controlId==fullArr[p].id){
                control.appendChild(selected);
                if(movePrev){
                    movePrev.innerHTML = '';
                }
                localStorage.setItem('hasChanged','N');
            }
        }
    }
    if(type=='bishop'&&!freeMov||type=='queen'&&!freeMov){
        for(var e=0; e<fullArr.length; e++){
            if(controlId==fullArr[e].id){
                for(var d=0; d<currDir.length; d++){
                    if(controlId==currDir[d]){
                        control.appendChild(selected);
                        if(movePrev){
                            movePrev.innerHTML = '';
                        }
                        localStorage.setItem('hasChanged','N');
                    }
                }
            }
        }
    }

    if(type=='king'){
        for(var m=0; m<kingsArray.length; m++){
            if(controlId==kingsArray[m]){
                control.appendChild(selected);
                if(movePrev){
                    movePrev.innerHTML = '';
                }
                if(selected.id=='bking'){
                    kingHasMoved = true;
                    localStorage.setItem("KingHasMoved", "Y");
                }
                localStorage.setItem('hasChanged','N');    
            }
        }
    }

    if(type=='horse'&&freeMov){
        for(var n=0; n<horseArr.length; n++){
            // console.log("HORSE: "+horseArr[n]+" controlId: "+controlId)
            if(controlId==horseArr[n]){
                control.appendChild(selected);
                if(movePrev){
                    movePrev.innerHTML = '';
                }
                localStorage.setItem('hasChanged','N');
            }
        }
    }
    if(type=='horse'&&!freeMov){
        for(var f=0; f<horseArr.length; f++){
            if(controlId==horseArr[f]){
                for(var g=0; g<currDir.length; g++){
                    if(controlId==currDir[g]){
                        control.appendChild(selected);
                        if(movePrev){
                            movePrev.innerHTML = '';
                        }
                        localStorage.setItem('hasChanged','N');
                    }
                }
            }
        }
    }
    //console.log("in move to pawn: "+type+" - "+freeMov);
    if(type=='pawn'&&freeMov){
        if(uniqPawn&&!isPawnFront){
            if(I-2>-1&&!isPawnFront2){
                //console.log("in move to pawn: "+controlId+" - "+I+" - "+J+" - "+boardMatrix[I-2][J]);
                if(controlId==boardMatrix[I-2][J]){
                    control.appendChild(selected);
                    if(movePrev){
                        movePrev.innerHTML = '';
                    } 
                    pawnIdArr.push(selected.id);
                    localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
                    localStorage.setItem('hasChanged','N');
                }
            }
            if(I-1>-1){
                if(controlId==boardMatrix[I-1][J]){
                    control.appendChild(selected);
                    if(movePrev){
                        movePrev.innerHTML = '';
                    }
                    pawnIdArr.push(selected.id);
                    localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
                    localStorage.setItem('hasChanged','N'); 
                }
            } 
        }
        if(!uniqPawn&&!isPawnFront){
            if(I-1>-1){
                if(controlId==boardMatrix[I-1][J]){
                    //console.log('hey man');
                    control.appendChild(selected);
                    if(movePrev){
                        movePrev.innerHTML = '';
                    }
                    pawnIdArr.push(selected.id);
                    localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
                    localStorage.setItem('hasChanged','N');
                    if(pawnEndNum!=null){
                        if(controlId==boardMatrix[0][pawnEndNum]){
                            var queen_id = getQueenId();
                            var queenNode = document.createElement('DIV');
                            queenNode.classList.add("blackPiece");
                            queenNode.classList.add("queen");
                            queenNode.id = queen_id;
                            queenNode.onclick = (theHuman).remove(queen_id);
                            control.appendChild(queenNode);
                        }
                    }
                }
            }
        }
    }
    //console.log('can choose: '+canChoose+' - '+placeId);
    if(type=='pawn'&&!freeMov){
        if(uniqPawn&&!isPawnFront){
            if(I-2>-1&&!isPawnFront2){
                if(controlId==boardMatrix[I-2][J]){
                    for(var h=0; h<currDir.length; h++){
                        if(controlId==currDir[h]){
                            control.appendChild(selected);
                            if(movePrev){
                                movePrev.innerHTML = '';
                            }
                            pawnIdArr.push(selected.id);
                            localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
                            localStorage.setItem('hasChanged','N');
                        }
                    }
                }
            }
            if(I-1>-1){
                if(controlId==boardMatrix[I-1][J]){
                   for(var s=0; s<currDir.length; s++){
                        if(controlId==currDir[s]){
                            control.appendChild(selected);
                            if(movePrev){
                                movePrev.innerHTML = '';
                            }
                            pawnIdArr.push(selected.id);
                            localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
                            localStorage.setItem('hasChanged','N');
                        }
                    }
                }
            } 
        }
        if(!uniqPawn&&!isPawnFront){
            if(I-1>-1){
                if(controlId==boardMatrix[I-1][J]){
                    for(var t=0; t<currDir.length; t++){
                        if(controlId==currDir[t]){
                            control.appendChild(selected);
                            if(movePrev){
                                movePrev.innerHTML = '';
                            }
                            pawnIdArr.push(selected.id);
                            localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
                            localStorage.setItem('hasChanged','N');
                            if(pawnEndNum!=null){
                                if(controlId==boardMatrix[0][pawnEndNum]){
                                    var queen_id = getQueenId();
                                    var queenNode = document.createElement('DIV');
                                    queenNode.classList.add("blackPiece");
                                    queenNode.classList.add("queen");
                                    queenNode.id = queen_id;
                                    queenNode.onclick = (theHuman).remove(queen_id);
                                    control.appendChild(queenNode);
                                }
                            }
                        }
                    }
                }
            }
        }
    
    }
 
    // console.log("in move to - rook1HasMoved: "+localStorage.getItem("Rook1HasMoved")+" rook2HasMoved: "+localStorage.getItem("Rook2HasMoved")+" kingHasMoved: "+localStorage.getItem("KingHasMoved")+" pawnIdArr: "+localStorage.getItem("PawnIDArray"));
}
}
}


this.remove = function(controlId){
    var newVal = localStorage.getItem('hasChanged');
    if(newVal == 'Y'){
    var control = document.getElementById(controlId);
    var parent = control.parentNode;
    var parentId = parent.id;
    var canChoose = false;
    // console.log("hello remove");
    var nestedPieces = pieces.children;
    
    for(var q=0; q<nestedPieces.length; q++){
        //console.log("piece id: "+nestedPieces[q].id);
        nonrepeatremovedArr(nestedPieces[q].id);
    }
    // console.log("nested guys: "+nestedPieceIds);

    localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
    localStorage.setItem("RemovedPiecesList", JSON.stringify(nestedPieceIds));
    localStorage.setItem("KingHasMoved", localStorage.getItem("KingHasMoved"));
    localStorage.setItem("Rook1HasMoved", localStorage.getItem("Rook1HasMoved"));
    localStorage.setItem("Rook2HasMoved", localStorage.getItem("Rook2HasMoved"));

    var Prev = document.getElementById(prev);
    var movePrev = undefined;
    //console.log('prev: '+prev);
    for(var f=0; f<allIdArr.length; f++){
        if(allIdArr[f]===controlId&&!control.hasChildNodes()){
            movePrev = Prev;
            allIdArr = [];
            break;
        }
    }

    if(type=='rook'&&freeMov||type=='queen'&&freeMov){
        for(var a=right; a<=left; a++){
            if(a<8&&a>-1){
                if(parentId==boardMatrix[I][a]){
                    pieces.appendChild(control);
                    parent.innerHTML = '';
                    parent.appendChild(selected);
                    if(selected.id=='brook1'){
                        rook1HasMoved = true;
                        localStorage.setItem("Rook1HasMoved", "Y");
                    }
                      if(selected.id=='brook2'){
                        rook2HasMoved = true;
                        localStorage.setItem("Rook2HasMoved", "Y");
                    }
                    localStorage.setItem('hasChanged','N');
                }
            }
        }
        for(var b=up; b<=down; b++){
            if(b<8&&b>-1){                    
                if(parentId==boardMatrix[b][J]){
                    pieces.appendChild(control);
                    parent.innerHTML = '';
                    parent.appendChild(selected);
                    if(selected.id=='brook1'){
                        rook1HasMoved = true;
                        localStorage.setItem("Rook1HasMoved", "Y");
                    }
                      if(selected.id=='brook2'){
                        rook2HasMoved = true;
                        localStorage.setItem("Rook2HasMoved", "Y");
                    }
                    localStorage.setItem('hasChanged','N');
                }
            }
        }
        // nestedPieceIds = [];
        nestedPieces = pieces.children;
        for(var q=0; q<nestedPieces.length; q++){
            nonrepeatremovedArr(nestedPieces[q].id);
        }
        localStorage.setItem("RemovedPiecesList", JSON.stringify(nestedPieceIds));
    }

    if(type=='bishop'&&freeMov||type=='queen'&&freeMov){
        for(var c=0; c<swtone.length; c++){;
            if(parentId==swtone[c].id){
                pieces.appendChild(control);
                parent.innerHTML = '';
                parent.appendChild(selected);
                localStorage.setItem('hasChanged','N');
            }
        }
        for(var d=0; d<nwtose.length; d++){;
            if(parentId==nwtose[d].id){
                pieces.appendChild(control);
                parent.innerHTML = '';
                parent.appendChild(selected);
                localStorage.setItem('hasChanged','N');
            }
        }
        // nestedPieceIds = [];
        nestedPieces = pieces.children;
        for(var q=0; q<nestedPieces.length; q++){
            nonrepeatremovedArr(nestedPieces[q].id);
        }
        localStorage.setItem("RemovedPiecesList", JSON.stringify(nestedPieceIds));
    }
    if(type=='rook'&&!freeMov||type=='queen'&&!freeMov){
        for(var j=right; j<=left; j++){
            if(j<8&&j>-1){
                if(parentId==boardMatrix[I][j]){
                    //console.log('parentId: '+parentId+' attacker: '+attacker);
                    if(parentId==attacker||parentId==guardAttack){
                        pieces.appendChild(control);
                        parent.innerHTML = '';
                        parent.appendChild(selected);
                        allIdArr.push(placeId);
                        if(selected.id=='brook1'){
                            rook1HasMoved = true;
                            localStorage.setItem("Rook1HasMoved", "Y");
                        }
                        if(selected.id=='brook2'){
                            rook2HasMoved = true;
                            localStorage.setItem("Rook2HasMoved", "Y");
                        }
                        //console.log('hello remove attacker: '+parent.innerHTML+' - '+parent.id);
                        localStorage.setItem('hasChanged','N');
                    }
                }
            }
        }
        for(var i=up; i<=down; i++){
            if(i<8&&i>-1){
                if(parentId==boardMatrix[i][J]){
                    if(parentId==attacker||parentId==guardAttack){
                        pieces.appendChild(control);
                        parent.innerHTML = '';
                        parent.appendChild(selected);
                        allIdArr.push(placeId);
                        if(selected.id=='brook1'){
                            rook1HasMoved = true;
                            localStorage.setItem("Rook1HasMoved", "Y");
                        }
                        if(selected.id=='brook2'){
                            rook2HasMoved = true;
                            localStorage.setItem("Rook2HasMoved", "Y");
                        }
                        localStorage.setItem('hasChanged','N');
                    }
                }
            }
        }
        // nestedPieceIds = [];
        nestedPieces = pieces.children;
        for(var q=0; q<nestedPieces.length; q++){
            nonrepeatremovedArr(nestedPieces[q].id);
        }
        localStorage.setItem("RemovedPiecesList", JSON.stringify(nestedPieceIds));
    }

    if(type=='bishop'&&!freeMov||type=='queen'&&!freeMov){
        for(var p=0; p<swtone.length; p++){;
            if(parentId==swtone[p].id){
                if(parentId==attacker||parentId==guardAttack){
                    pieces.appendChild(control);
                    parent.innerHTML = '';
                    parent.appendChild(selected);
                    allIdArr.push(placeId);
                    localStorage.setItem('hasChanged','N');
                }
            }
        }
        for(var q=0; q<nwtose.length; q++){;
            if(parentId==nwtose[q].id){
                if(parentId==attacker||parentId==guardAttack){
                    pieces.appendChild(control);
                    parent.innerHTML = '';
                    parent.appendChild(selected);
                    allIdArr.push(placeId);
                    localStorage.setItem('hasChanged','N');
                }
            }
        }
        // nestedPieceIds = [];
        nestedPieces = pieces.children;
        for(var q=0; q<nestedPieces.length; q++){
            nonrepeatremovedArr(nestedPieces[q].id);
        }
        localStorage.setItem("RemovedPiecesList", JSON.stringify(nestedPieceIds));
    }
   
    if(type=='king'){
        for(var m=0; m<kingsArray.length; m++){
            if(parentId==kingsArray[m]){
                pieces.appendChild(control);
                parent.innerHTML = '';
                parent.appendChild(selected);
                if(selected.id=='bking'){
                    kingHasMoved = true;
                    localStorage.setItem("KingHasMoved", "Y");
                }
                localStorage.setItem('hasChanged','N');
            }
        }
        // nestedPieceIds = [];
        nestedPieces = pieces.children;
        for(var q=0; q<nestedPieces.length; q++){
            nonrepeatremovedArr(nestedPieces[q].id);
        }
        localStorage.setItem("RemovedPiecesList", JSON.stringify(nestedPieceIds));
    }

    if(type=='horse'&&freeMov){
        for(var n=0; n<horseArr.length; n++){
            if(parentId==horseArr[n]){
                pieces.appendChild(control);
                parent.innerHTML = '';
                allIdArr.push(parentId);
                parent.appendChild(selected);
                localStorage.setItem('hasChanged','N');
            }
        }
        // nestedPieceIds = [];
        nestedPieces = pieces.children;
        for(var q=0; q<nestedPieces.length; q++){
            nonrepeatremovedArr(nestedPieces[q].id);
        }
        localStorage.setItem("RemovedPiecesList", JSON.stringify(nestedPieceIds));
    }
    if(type=='horse'&&!freeMov){
        for(var n=0; n<horseArr.length; n++){
            if(parentId==horseArr[n]){
                if(parentId==attacker||parentId==guardAttack){
                    pieces.appendChild(control);
                    parent.innerHTML = '';
                    parent.appendChild(selected);
                    localStorage.setItem('hasChanged','N');
                }
            }
        }
        // nestedPieceIds = [];
        nestedPieces = pieces.children;
        for(var q=0; q<nestedPieces.length; q++){
            nonrepeatremovedArr(nestedPieces[q].id);
        }
        localStorage.setItem("RemovedPiecesList", JSON.stringify(nestedPieceIds));
    }
    // console.log("remove pawn: "+parentId+' - '+pawntr+' - '+pawntl+' - '+pawntrEndNum+' - '+pawntlEndNum);
    if(type=='pawn'&&freeMov){
        if(parentId==pawntr){
            pieces.appendChild(control);
            parent.innerHTML = '';
            parent.appendChild(selected);
            pawnIdArr.push(selected.id);
            localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
            // console.log("remove pawn tr: "+parentId+' - '+pawntr+' - '+pawntrEndNum);
            if(pawntrEndNum!=null){
                if(parentId==boardMatrix[0][pawntrEndNum]){
                    parent.innerHTML = '';
                    var queen_id = getQueenId();
                    // console.log("queen id: "+queen_id);
                    var queenNode = document.createElement('DIV');
                    queenNode.classList.add("blackPiece");
                    queenNode.classList.add("queen");
                    queenNode.id = queen_id;
                    queenNode.onclick = function() {(theHuman).remove(queen_id)};
                    parent.appendChild(queenNode);
                }
            }
            localStorage.setItem('hasChanged','N');
            //console.log('pr can choose: '+canChoose+' '+parentId);
        }
        if(parentId==pawntl){
            pieces.appendChild(control);
            parent.innerHTML = '';
            parent.appendChild(selected);
            // console.log('pawn end num: '+pawntlEndNum);
            pawnIdArr.push(selected.id);
            localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
            if(pawntlEndNum!=null){
                //console.log('pawn end num id: '+boardMatrix[7][pawntlEndNum]+' p: '+parentId);
                if(parentId==boardMatrix[0][pawntlEndNum]){
                    parent.innerHTML = '';
                    var queen_id = getQueenId();
                    // console.log("queen id: "+queen_id);
                    var queenNode = document.createElement('DIV');
                    queenNode.classList.add("blackPiece");
                    queenNode.classList.add("queen");
                    queenNode.id = queen_id;
                    queenNode.onclick = function() {(theHuman).remove(queen_id)};
                    parent.appendChild(queenNode);
                }
            }
            localStorage.setItem('hasChanged','N');
            //console.log('pl can choose: '+canChoose+' '+parentId);
        }
        // nestedPieceIds = [];
        nestedPieces = pieces.children;
        for(var q=0; q<nestedPieces.length; q++){
            nonrepeatremovedArr(nestedPieces[q].id);
        }
        localStorage.setItem("RemovedPiecesList", JSON.stringify(nestedPieceIds));
    }
    if(type=='pawn'&&!freeMov){
        if(parentId==pawntr){
            if(parentId==attacker||parentId==guardAttack){
                pieces.appendChild(control);
                parent.innerHTML = '';
                parent.appendChild(selected);
                pawnIdArr.push(selected.id);
                localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
                allIdArr.push(placeId);
                
                if(pawntrEndNum!=null){
                    if(parentId==boardMatrix[0][pawntrEndNum]){
                        parent.innerHTML = '';
                        var queen_id = getQueenId();
                        // console.log("queen id: "+queen_id);
                        var queenNode = document.createElement('DIV');
                        queenNode.classList.add("blackPiece");
                        queenNode.classList.add("queen");
                        queenNode.id = queen_id;
                        queenNode.onclick = function() {(theHuman).remove(queen_id)};
                        parent.appendChild(queenNode);
                    }
                }
                localStorage.setItem('hasChanged','N');
            }
        }
        if(parentId==pawntl){
            if(parentId==attacker||parentId==guardAttack){
                pieces.appendChild(control);
                parent.innerHTML = '';
                parent.appendChild(selected);
                allIdArr.push(placeId);
                pawnIdArr.push(selected.id);
                localStorage.setItem("PawnIDArray", JSON.stringify(pawnIdArr));
                if(pawntlEndNum!=null){
                    if(parentId==boardMatrix[0][pawntlEndNum]){
                        parent.innerHTML = '';
                        var queen_id = getQueenId();
                        // console.log("queen id: "+queen_id);
                        var queenNode = document.createElement('DIV');
                        queenNode.classList.add("blackPiece");
                        queenNode.classList.add("queen");
                        queenNode.id = queen_id;
                        queenNode.onclick = function() {(theHuman).remove(queen_id)};
                        parent.appendChild(queenNode);
                    }
                }
                localStorage.setItem('hasChanged','N');
            }
        }
        // nestedPieceIds = [];
        nestedPieces = pieces.children;
        for(var q=0; q<nestedPieces.length; q++){
            nonrepeatremovedArr(nestedPieces[q].id);
        }
        localStorage.setItem("RemovedPiecesList", JSON.stringify(nestedPieceIds));
    }
   
}
}
}  

