localStorage.setItem('hasChanged', 'N');
localStorage.setItem('hasSelected', 'N');
localStorage.setItem('FinishedMove', 'N');

var stateMatrix = [[{ pieceId: "wrook1", placeId: "r1A"},{ pieceId: "whorse1", placeId: "r1B"},{ pieceId: "wbishop1", placeId: "r1C"},
					{ pieceId: "wqueen", placeId: "r1D"},{ pieceId: "wking", placeId: "r1E"},{ pieceId: "wbishop2", placeId: "r1F"},
					{ pieceId: "whorse2", placeId: "r1G"},{ pieceId: "wrook2", placeId: "r1H"}],
				   [{ pieceId: "wpawn1", placeId: "r2A"},{ pieceId: "wpawn2", placeId: "r2B"},{ pieceId: "wpawn3", placeId: "r2C"},
					{ pieceId: "wpawn4", placeId: "r2D"},{ pieceId: "wpawn5", placeId: "r2E"},{ pieceId: "wpawn6", placeId: "r2F"},
					{ pieceId: "wpawn7", placeId: "r2G"},{ pieceId: "wpawn8", placeId: "r2H"}],
				   [ {pieceId: "", placeId: "r3A"}, {pieceId: "", placeId: "r3B"}, {pieceId: "", placeId: "r3C"},
				     {pieceId: "", placeId: "r3D"}, {pieceId: "", placeId: "r3E"}, {pieceId: "", placeId: "r3F"}, 
				     {pieceId: "", placeId: "r3G"}, {pieceId: "", placeId: "r3H"} ],
				   [ {pieceId: "", placeId: "r4A"}, {pieceId: "", placeId: "r4B"}, {pieceId: "", placeId: "r4C"},
				     {pieceId: "", placeId: "r4D"}, {pieceId: "", placeId: "r4E"}, {pieceId: "", placeId: "r4F"}, 
				     {pieceId: "", placeId: "r4G"}, {pieceId: "", placeId: "r4H"} ], 
				   [ {pieceId: "", placeId: "r5A"}, {pieceId: "", placeId: "r5B"}, {pieceId: "", placeId: "r5C"},
				     {pieceId: "", placeId: "r5D"}, {pieceId: "", placeId: "r5E"}, {pieceId: "", placeId: "r5F"}, 
				     {pieceId: "", placeId: "r5G"}, {pieceId: "", placeId: "r5H"} ],
				   [ {pieceId: "", placeId: "r6A"}, {pieceId: "", placeId: "r6B"}, {pieceId: "", placeId: "r6C"},
				     {pieceId: "", placeId: "r6D"}, {pieceId: "", placeId: "r6E"}, {pieceId: "", placeId: "r6F"}, 
				     {pieceId: "", placeId: "r6G"}, {pieceId: "", placeId: "r6H"} ],
				   [{ pieceId: "bpawn1", placeId: "r7A"},{ pieceId: "bpawn2", placeId: "r7B"},{ pieceId: "bpawn3", placeId: "r7C"},
					{ pieceId: "bpawn4", placeId: "r7D"},{ pieceId: "bpawn5", placeId: "r7E"},{ pieceId: "bpawn6", placeId: "r7F"},
					{ pieceId: "bpawn7", placeId: "r7G"},{ pieceId: "bpawn8", placeId: "r7H"}],
				   [{ pieceId: "brook1", placeId: "r8A"},{ pieceId: "bhorse1", placeId: "r8B"},{ pieceId: "bbishop1", placeId: "r8C"},
					{ pieceId: "bqueen", placeId: "r8D"},{ pieceId: "bking", placeId: "r8E"},{ pieceId: "bbishop2", placeId: "r8F"},
					{ pieceId: "bhorse2", placeId: "r8G"},{ pieceId: "brook2", placeId: "r8H"}]			   
				   ];

localStorage.setItem("StateMatrix", JSON.stringify(stateMatrix));

localStorage.setItem("CurrentCompSelect", "empty");

localStorage.setItem("CurrentCompMove", "empty");

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
localStorage.setItem("FreeMove", "Y");

localStorage.setItem("CurrentDirectionArray", JSON.stringify([]));
localStorage.setItem("CurrentAttackerArray", JSON.stringify([]));
localStorage.setItem("SaverArray", JSON.stringify([]));
localStorage.setItem("AttackerArray", JSON.stringify([]));
localStorage.setItem("InGuard", "N");
localStorage.setItem("PieceInGuard", "");
localStorage.setItem("FreeMovementLength", "");
localStorage.setItem("CanSaveKing", "N");

localStorage.setItem("PawnIDArray", JSON.stringify([]));
localStorage.setItem("KingHasMoved", "N");
localStorage.setItem("Rook1HasMoved", "N");
localStorage.setItem("Rook2HasMoved", "N");
localStorage.setItem("RemovedPiecesList", JSON.stringify([]));
