/*Lessons:
 Use constants as often as possible
don't end statements
 ' " ` are string types using ` ${} ` allows you run code within a string
functions can be called at any place in the script (function at bottom called higher up)
functions have full access to outside of a function, but not the other way around
*/

const defaultResult = 0;
let currentResult = defaultResult;
let logEntries = [];

//gets input from input field
function getUserNumberInput() {
  return parseInt(userInput.value);
}

// Generated and writes calculation log
function createAndWriteOutput(operator, resultBeforeCalc, calcNumber) {
  const calcDescription = `${resultBeforeCalc} ${operator} ${calcNumber}`;
  outputResult(currentResult, calcDescription); // from vendor file
}

function writeToLog(operationId, prevResult, operationNumber, newResult) {
  const logEntry = {
    // generate an object to store information inside of an array
    operation: operationId,
    prevResult: prevResult,
    number: operationNumber,
    result: newResult,
  };
  logEntries.push(logEntry);
  console.log(logEntries); //arrays start at index 0
}

function add() {
  const enteredNumber = parseInt(userInput.value); //cleans up code if needing to rename the userInput variable
  const initialResult = currentResult;
  currentResult += enteredNumber; // can replace parseInt with +, parseFloat deals with floating numbers
  //   alert(`The result is ${result}`); // shows alert pop up
  //   return result; //useful for getting data out of a function
  //outputResult(currentResult, ); // moved here so it outputs when function runs (replaced by createandwriteoutput function)
  createAndWriteOutput("+", initialResult, enteredNumber);
  writeToLog("add", initialResult, enteredNumber, currentResult);
  console.log(logEntry.operation);
}

function subtract() {
  const enteredNumber = parseInt(userInput.value); // can copy add and change modifiers
  const initialResult = currentResult;
  currentResult -= enteredNumber; // also written as currentResult = currentResult - enteredNumber;
  createAndWriteOutput("-", initialResult, enteredNumber);
  writeToLog("subtract", initialResult, enteredNumber, currentResult);
  console.log(logEntry.operation);
}

function multiply() {
  const enteredNumber = parseInt(userInput.value); // can copy add and change modifiers
  const initialResult = currentResult;
  currentResult *= enteredNumber;
  createAndWriteOutput("*", initialResult, enteredNumber);
  writeToLog("multiply", initialResult, enteredNumber, currentResult);
  console.log(logEntry.operation);
}

function divide() {
  const enteredNumber = parseInt(userInput.value); // can copy add and change modifiers
  const initialResult = currentResult;
  currentResult /= enteredNumber;
  createAndWriteOutput("/", initialResult, enteredNumber);
  writeToLog("divide", initialResult, enteredNumber, currentResult);
  console.log(logEntry.operation);
}

//to reset calculator
function clearinputs() {
  let enteredNumber = 0;
  const initialResult = 0;
  currentResult = enteredNumber;
  createAndWriteOutput("0", "", "");
  writeToLog("cleared", initialResult, enteredNumber, currentResult);
  console.log(logEntry.operation);
}

//currentResult = add(1,2);
//let calculationDescription = `(${defaultResult} + 10) * 3 / 2 - 1`;

addBtn.addEventListener("click", add);
subtractBtn.addEventListener("click", subtract);
multiplyBtn.addEventListener("click", multiply);
divideBtn.addEventListener("click", divide);
clearBtn.addEventListener("click", clearinputs);
