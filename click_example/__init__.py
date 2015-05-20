from __future__ import print_function

import click


@click.group()
@click.argument('main_argument_one', type=str)
@click.option('--option-one', type=str, help="This is an option for the "
              "main command!")
@click.pass_context
def main(ctx, main_argument_one, option_one):
    """
    The main command (what you run!)
    """

    print("Main argument: %s" % main_argument_one)
    print("Main option 1: %s" % option_one)

    ctx.obj= {
        "main_argument_one": main_argument_one
    }


@click.command()
@click.argument('foo_argument_one', type=str)
@click.option('--option-one', type=str, help="This is an option!",
              default='Default option')
@click.option('--enable-option-two', help="This is a boolean option!",
              is_flag=True)
@click.pass_context
def foo(ctx, foo_argument_one, option_one, enable_option_two):
    """
    Performs a foo!
    """

    print("Foo argument: %s" % foo_argument_one)
    print("Foo option 1: %s" % option_one)

    if enable_option_two:
        print("Option 2 enabled!")


@click.command()
@click.argument('bar_argument_one', type=str)
@click.argument('bar_argument_two', type=str)
@click.option('--option-one', type=str, help="This option helps bar!")
@click.pass_context
def bar(ctx, bar_argument_one, bar_argument_two, option_one):
    """
    Executes one bar!
    """

    print("Bar argument 1: %s" % bar_argument_one)
    print("Bar argument 2: %s" % bar_argument_two)
    print("Bar option 1: %s" % option_one)

    print("Main argument 1 again: %s" % ctx.obj['main_argument_one'])

main.add_command(foo)
main.add_command(bar)
