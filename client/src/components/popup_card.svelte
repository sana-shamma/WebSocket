<script>
    export let showCard;
    import InputField from "../components/inputField.svelte";
    import Button from "../components/button.svelte";
    let title = "";
    let content = "" ;
    import MyWords from "../api/my_words";
    import { onMount } from "svelte"
    let myWord;
    onMount(() => {
        myWord = new MyWords();
    });

    async function addWord(){
        myWord.add_word(title,content );
        showCard = false;
    }

  </script>
  
  {#if showCard}
    <div id="background" on:click|self >
      <div id="popup-message">
        <InputField bind:value={title} id="title" title="Title"/>
        <InputField bind:value={content} id="content" title="Content"/>
        <Button id="add" value="Add" onClick={addWord}/>
      </div>
    </div>
  {/if}
  
  <style>
    #background {
      width: 100vw;
      height: 100vh;
      position: fixed;
      z-index: 2000;
      background-color: rgba(0, 0, 0, 0.8);
    }
    #popup-message {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%,-50%);
      border-radius: 10px;
      width: 200px;
      height: 200px;
      padding: 30px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
      background-color: white;
      box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); 
    }
  </style>