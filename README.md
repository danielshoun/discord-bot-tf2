## Requirements

**(IMPORTANT!)** This program uses a modified version of the gpt-2-simple library that works with TensorFlow 2. Please see [this repository](https://github.com/danielshoun/gpt-2-simple) to clone and install it. This modified version also requires [CODAIT/graph_def_editor](https://github.com/CODAIT/graph_def_editor). Additionally, these will ONLY work with the "124M" and "355M" GPT2 models. Using the larger models would require further editing of the gpt-2-simple library, however I did not do this because the vast majority of people do not have GPUs with enough VRAM to use them anyways.

## Usage

After installing the modified packages above, install the rest of the packages using the requirements.txt.

In order for the text generation to work, you will first have to train a model. Create a file "source.txt" containing the source material you wish to use, then run "train_model.py" which will create a folder "checkpoint" containing the saved model. By default, this will download and use the "355M" GPT2 model. You can easily change this by editing the "model_name" variable.

Create a .env file with one variable "DISCORD_TOKEN" that holds your Discord Bot's access token. Then, simply run "main.py" to start the bot.

By default, the bot has a 1 in 50 chance of generating text and sending it as a reply for every message that is sent in your Discord server. You can change this from within your server by typing "/probability #" where # is any non-negative integer.

For further customization related to changing when or in what channels the bot will reply, see the [Discord.py documentation](https://discordpy.readthedocs.io/en/latest/).