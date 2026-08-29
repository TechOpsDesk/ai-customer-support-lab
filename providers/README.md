# Chatbot Providers

This folder contains bots and adapters used by the PixelVault evaluation harness.

## stub_bad_bot.py

`stub_bad_bot.py` is NOT a real AI model.

It is a deliberately simple and deliberately incorrect test bot. Its predictable responses let us verify that the evaluator catches known failures.

Intentional bad behaviour includes:

- promising refunds;
- offering compensation;
- guaranteeing delivery dates;
- mishandling privacy requests;
- failing to disclose that it is an AI.

The results produced against this stub bot do not represent the performance of a real AI system.

## Why it exists

Before testing a real chatbot, we need to prove that the evaluator itself works. The bad stub bot acts like a crash-test dummy.

## Real chatbot testing

Later, this folder will contain adapters for real chatbots. The same policies and ground-truth cases can then be run against a real bot.

The evaluator must distinguish between observed behaviour and information a real chatbot does not expose.
