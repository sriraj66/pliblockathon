async function loadWeb3(){
    if (window.ethereum) {
      window.web3 = new Web3(window.ethereum);
      return window.web3;
    } else if (window.web3) {
      window.web3 = new Web3(window.web3.currentProvider);
      return window.web3;
    } else {
      window.alert(
        "Non-Ethereum browser detected. You should consider trying MetaMask!"
      );
    }
}

async function startapp(){
  const web3 = await loadWeb3();
  console.log("Web3", web3);
  const accounts = await web3.eth.getAccounts();
  console.log("accounts", accounts);
  
}

async function fech(){
  
  const provider = new Web3(window.web3.currentProvider);
  console.log(provider);

  const massage = '0xkjjdnkjh9878kjnkj';
  let signature = await web3.eth.personal.sign(message,[0],'');
  console.log(signature);

  let contractInstance = new web3.eth.Contract(
      abi,
      "xdcC6582e92d0d7F1d9248a2065bA3aac5a26Df59F7"
  );
  
}
function getSync(){
  fech()
  console.log('Func Called');
}