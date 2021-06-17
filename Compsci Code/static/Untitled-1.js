//  frame rate related variables
var maxFPS = 30;
var frameInterval = 1000 / maxFPS;
var timePrevFrame = Date.now();

//  freefall properties
var gravity = 4;
var jumpPower = 24;
var pixelPerFrame = 0;
var maxPixelPerFrame = 20;

var score = document.querySelector("#score");

//  player element & properties
var player = document.querySelector("#player");
var playerTop = 300;
var playerLeft = 200;
var playerWidth = 35;
var playerHeight = 64;
var playerInAir = true;
var playerActive = true;

//  terrain element & properties
var terrainContainer = document.querySelector("#terrainContainer");
var blockSize = 64;
var terrainLeft = 0;
var terrainScroll = 7.5;
var terrain = [2, 1, 1, 1, 2, 2, 3, 3,4,4,4,3,5,6,3,2,5,3,4,6,3,5,6,6,6,8,5,5,5,5,5,5,5,5,6,5,6,6,6,5,6,6,6,6,6,4,4,4,4,4,4,4,4,4,5,5,5,5,3,3,3,4,4,4,6,6,6,4,5,5,5,5,7,7,6,5,4,1,1,1,1,3,3,3,4,4,6,6,6,4,1,1,1,1,3,3,2,2,1,2,2,2,1];
var coinPositions =  [0, 1, 2, 1, 3, 3,5,6,5,4,6,7,8,5,4,5,4,6,5];
var coins;

//  set initial player position
player.style.left = playerLeft + "px";

//  generate terrain
generateTerrain();
//  start the game loop
gameLoop();

onkeydown = jump;
onkeypress = fly;



// =============================== //
// ========== FUNCTIONS ========== //
// =============================== //

function generateTerrain() {
    //  create a column of blocks for each number in the terrain array
    terrain.forEach((columnSize, columnIndex) => {
        //  create an array for each number in the terrain array
        var newBlocks = new Array(columnSize).fill();
        //  calculate & store the left position for each column
        var columnLeft = playerLeft + columnIndex * blockSize;
        //  determine if coloumnSize is the last number in the tarrain array
        var finalColumn = columnIndex == terrain.length - 1;

        newBlocks.forEach((newBlock, blockIndex) => {
            //  create a new block
            newBlock = document.createElement("div");
            //  add new block to the terrain container
            terrainContainer.appendChild(newBlock);

            //  calculate and store the bottom position for each block
            var blockBottom = (columnSize - blockIndex - 1) * blockSize;

            newBlock.style.left = columnLeft + "px";
            newBlock.style.bottom = blockBottom + "px";

            newBlock.className = "block";

            //  determine if a block is the first in that column
            if (blockIndex === 0) {
                newBlock.className = "block top";
                
                if (finalColumn) {
                    finishSign.style.left = newBlock.style.left;
                    finishSign.style.bottom = blockBottom + blockSize + "px";
                }
            }
        });
        
        if (coinPositions[columnIndex] > 0) {
            var newCoin = document.createElement("div");
            terrainContainer.appendChild(newCoin);
            
            newCoin.className = "coin";
            
            //  calculate the difference in width and height between the coin and a block
            //  then divides it by 2
            var widthDiff = (blockSize - newCoin.offsetWidth) / 2;
            var heightDiff = (blockSize - newCoin.offsetHeight) / 2;
            
            var floatHeight = coinPositions[columnIndex] * blockSize;

            newCoin.style.left = columnLeft + widthDiff + "px";
            newCoin.style.bottom = floatHeight + heightDiff + "px";
        }
    });
    
    //  store all coin images into an array
    coins = document.querySelectorAll(".coin");
    totalCoins.innerText = coins.length;
}

function jump() {
    if (playerInAir === false && event.code == "Space") {
        pixelPerFrame -= jumpPower+10;
        player.className = "jump";
    }
}



function gameLoop() {
    //  store the current time when this function is called
    var currentTime = Date.now();
    //  calculate the elapsed time since the previous frame
    var elapsed = currentTime - timePrevFrame;

    //  determine if it is time to draw another frame
    if (elapsed > frameInterval) {
        //  update timePrevFrame
        timePrevFrame = currentTime - (elapsed % frameInterval);
        //  call the actionPerFrame function, i.e. draw a new frame
        requestAnimationFrame(actionPerFrame);
    }

    //  call gameLoop function again
    requestAnimationFrame(gameLoop);
}

function actionPerFrame() {
    animateFreefall();

    if (playerActive) {
        animateTerrain();
        detectGroundCollision();
        detectCoinCollection();
        detectFinishSign();
    }

    detectOutOfFrame();

    player.style.top = playerTop + "px";
}

function animateFreefall() {
    //  determine if pixelPerFrame has reached maximum value
    if (playerInAir && pixelPerFrame < maxPixelPerFrame) {
        //  increase the rate of falling, i.e. pixelPerFrame
        pixelPerFrame += gravity;
    }

    //  modify player top position using pixelPerFrame
    playerTop += pixelPerFrame;
}

function animateTerrain() {
    terrainLeft -= terrainScroll;
    terrainContainer.style.left = terrainLeft + "px";
}

function detectGroundCollision() {
    //  assume no collision at the beginning of every frame
    var noCollision = true;
    //  store all block elements
    var blocks = document.querySelectorAll(".block");

    //  perform collision check on each block
    blocks.forEach(block => {
        //  calculate the minimum and maximum left position for a block
        //  that can collide with the player
        var minLeft = playerLeft - blockSize;
        var maxLeft = playerLeft + playerWidth;

        var blockLeft = block.offsetLeft + terrainLeft;

        //  remove border no longer colliding with player
        block.style.border = "none";

        //  determine if a block can collide with the player
        if (playerActive && blockLeft < maxLeft && blockLeft > minLeft) {
            var blockTop = block.offsetTop;

            //  calculate the maximum top position for the player
            //  before it collides with a block
            var maxTop = blockTop - playerHeight;

            //  determine if player is colliding with a block
            if (playerTop >= maxTop) {
                //  calculate the vertical distance between the player and a colliding block
                var vDist = playerTop + playerHeight - blockTop;

                //  determine if the distance is greater than the maximum freefall distance
                if (vDist > maxPixelPerFrame) {
                    playerCrash();
                    noCollision = true;
                }
                else {
                    //  prevent playerTop from exceeding maxTop
                    playerTop = maxTop;
                    //  stop the player from falling
                    pixelPerFrame = 0;
                    noCollision = false;

                    player.className = "run";

                    //  add border to visualise the block colliding with player
                    block.style.border = "dashed 1px black";
                }
            }
        }
    });
    
    playerInAir = noCollision;
}

function detectCoinCollection() {
    coins.forEach(coin => {
        if (coin.className == "coin") {
            var coinLeft = coin.offsetLeft + terrainContainer.offsetLeft;
            var coinTop = coin.offsetTop + terrainContainer.offsetTop;
            var coinWidth = coin.offsetWidth;
            var coinHeight = coin.offsetHeight;
            
            var collected =
                playerLeft + playerWidth > coinLeft &&
                playerLeft < coinLeft + coinWidth &&
                playerTop + playerHeight > coinTop &&
                playerTop < coinTop + coinHeight;
                
            if (collected) {
                var currentScore = Number(score.textContent);

                score.innerText = currentScore + 1;
                coin.classList.add("collected");
            }
        }
    });
}

function detectFinishSign() {
    var signLeft = finishSign.offsetLeft + terrainContainer.offsetLeft;
    var finished = playerLeft >= signLeft;
    
    if (finished && !playerInAir) {
        playerActive = false;
        
        if (confirm("You finished the level, play again?")) {
            resetGame();
        }
    }
}

function detectOutOfFrame() {
    var sceneHeight = document.querySelector("#scene").offsetHeight;
    //  define the condition when player touches the bottom edge of the scene
    var atBottomEdge = playerTop + playerHeight > sceneHeight;

    if (playerActive && atBottomEdge) {
        playerCrash();
    }
    else if (playerTop > sceneHeight) {
        resetGame();
    }
}

function playerCrash() {
    //  set pixelPerFrame to a negative value makes the character move up
    pixelPerFrame = -maxPixelPerFrame;
    player.className = "crash";
    playerActive = false;
}

function resetGame() {
    playerTop = 300;
    player.className = "jump";
    playerInAir = true;
    playerActive = true;
    pixelPerFrame = 0;
    terrainLeft = 0;
   score.innerText=1;
    
    coins.forEach(coin => coin.classList.remove("collected"));
}


function fly() { 
if(event.code=="KeyZ")  {
 
 playerTop = 70;
  playerTop = 69;
  playerTop = 68;
  playerTop = 67;
  playerTop = 66;
  playerTop = 65;
  playerTop = 64;
  playerTop = 63;
  playerTop = 62;
  playerTop = 60;
  playerTop = 57;
  playerTop = 55;
  playerTop = 50;
  playerTop = 45;
  playerTop = 42;
   playerTop = 39;
   playerTop = 36;
   playerTop = 33; playerTop = 20;
     terrainScroll= 10;
  gravity= -0.0001;
  
  
  player.className = "fly";
}


   
     
   
   



}

function reset() { 
     terrainScroll= 3;

playerTop = 300;



}
function BOOST() { 
  
score-=5;
  playerTop=20;
  gravity=1;
  
}

if (gravity=== 0) {


  gravity=2;

}

