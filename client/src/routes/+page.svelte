
<script>
    import { onMount } from "svelte";
    import Card from "../components/card.svelte";
    import Button from "../components/button.svelte";
    import PopupCard from "../components/popup_card.svelte";
    import MyWords from "../api/my_words.js";
    let myWord;
    let words;
    import {socket} from '../api/connections';

    onMount( () => {
        myWord = new MyWords();
    });
    
    let getAllWords = async () => {
    words = await myWord.get_all_words();
    socket.onmessage = (event) => {
    let data = JSON.parse(event.data);
    if (Array.isArray(data)) {
        words = data;
    }}
    };
    
    let showCard = false;
      const toggleCard = ()=>{
        showCard= !showCard;
    }
    
</script>
    
<PopupCard bind:showCard={showCard} on:click={toggleCard}/>
    
<header>
    <h1>Words Board</h1>
    <div id="buttons-comtainer">
        <Button onClick={toggleCard} id="add" value="+ Add a Word"/>
        <Button onClick={getAllWords} id="display" value="Display Words"/>
    </div>
</header>
    
<div id="board">
    {#if words}
        {#each words as word}
        <Card word={word["title"]} content={word["meaning"]}/>
        {/each}	
    {/if}
</div>
    
<style>
    header{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: rgb(135, 181, 222);
        padding: 10px;
    }
    #board{
        background-color: rgb(233, 240, 240);
        padding: 10px;
        display: flex;
        gap: 10px;
        height: 100vh;
    }
    h1{
        color: white;
    }
</style>
    