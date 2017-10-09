from invoke import task


@task(default=True)
def test(ctx):
    ctx.run("py.test")


# @task
# def clean(ctx):
#     ctx.run("rm -rf test/*.{conf,txt}")
