// https://freebitco.in/

// main values
var startValue = '0.00000001', // bit amount
	stopPercentage = 0.001, // percent of balance to bit
	maxWait = 3, // time sec
	stopped = false,
	stopBefore = 1,
	startTime = new Date,
	startBalance = deexponentize(parseFloat($('#balance').text()));


// buttons
var $loButton = $('#double_your_btc_bet_lo_button'),
	$hiButton = $('#double_your_btc_bet_hi_button');

// functions:
function multiply(){
	var current = $('#double_your_btc_stake').val();
	var multiply = (current * 2).toFixed(8);

	$('#double_your_btc_stake').val(multiply);
};

function getRandomWait(){
	var wait = Math.floor(Math.random() * maxWait) * 1000;
	console.log('Waiting for ' + wait + 'ms before next bet.');
	return wait;
};

function startGame(){
	console.log('Game started!');
	reset();
	$loButton.trigger('click');
};

function stopGame(){
	console.log('Game will stop soon! Let me finish.');
	stopped = true;
};

function reset(){
	$('#double_your_btc_stake').val(startValue);
};

function deexponentize(number){
	return number * 100000000;
};

function iHaveEnoughMoni(){
	var balance = deexponentize(parseFloat($('#balance').text()));
	var current = deexponentize($('#double_your_btc_stake').val());
	return ((balance)*2/100) * (current*2) > stopPercentage/100;
};

function stopBeforeRedirect(){
	var minutes = parseInt($('title').text());
	if (minutes < stopBefore){
		console.log('Approaching redirect! Stop the game so we don\'t get redirected while loosing.');
		stopGame();
		return true;
	}
	return false;
};

// Remove jackpot
$('.play_jackpot').prop("checked",false);

// Unbind old shit
$('#double_your_btc_bet_lose').unbind();
$('#double_your_btc_bet_win').unbind();

// Loser
$('#double_your_btc_bet_lose').bind('DOMSubtreeModified', function(event){
	if ($(event.currentTarget).is(':contains("lose")')) {
		console.log('You LOST! Multiplying your bet and betting again.');
		multiply();
		setTimeout(function(){
			$loButton.trigger('click');
		}, getRandomWait());
	}
});

// Winner
$('#double_your_btc_bet_win').bind('DOMSubtreeModified', function(event){
	if ($(event.currentTarget).is(':contains("win")')) {
		if (stopBeforeRedirect()) {
			return;
		}
		if (iHaveEnoughMoni()) {
			var balanceNow = (deexponentize(parseFloat($('#balance').text())) - startBalance).toFixed();
			var timeOut = ((new Date - startTime)/1000).toFixed();
			console.log('You WON! But don\'t be greedy. Restarting!');
			console.log('Profit is: ' + balanceNow + ' satoshi for ' + timeOut + 'sec.');
			reset();
			if (stopped) {
				stopped = false;
				return false;
			}
		} else {
			console.log('You WON! Betting again.');
		}

		setTimeout(function(){
			$loButton.trigger('click');
		}, getRandomWait());
	}
});

startGame();
//stopGame();