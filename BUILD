load("@io_bazel_rules_go//go:def.bzl", "go_binary", "go_library")
load("@rules_python//python:defs.bzl", "py_binary")
load("@bazel_gazelle//:def.bzl", "gazelle")

# gazelle:prefix github.com/grahamjenson/bazel-python-to-golang
gazelle(name = "gazelle")

py_binary(
    name = "main",
    srcs = ["main.py"],
    data = [":project"]
)

go_library(
    name = "project_lib",
    srcs = ["main.go"],
    cgo = True,
    importpath = "github.com/grahamjenson/bazel-python-to-golang",
)

go_binary(
    name = "project",
    embed = [":project_lib"],
    linkmode="c-shared",
    out="_golib.so"
)
