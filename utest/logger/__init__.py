__all__ = ['get_logger']

import sys
import logging
import inspect
from types import FrameType


def get_logger(logger_name: str | None = None) -> logging.Logger:
  """
  创建并配置日志器

  Args:
    logger_name: 日志器名称
  """
  if logger_name is None:
    this_frame = inspect.currentframe()
    prev_frame: FrameType | None = None
    if this_frame is not None:
      prev_frame = this_frame.f_back

    caller_module = inspect.getmodule(prev_frame)
    if caller_module is not None:
      logger_name = caller_module.__name__

  # 获取日志器
  logger = logging.getLogger(logger_name)

  # 如果日志器已经配置过则跳过
  if logger.handlers:
    return logger

  # 设置日志级别
  logger.setLevel(logging.DEBUG)

  # 创建格式化器
  formatter = logging.Formatter(
    fmt='%(asctime)s %(name)s %(levelname)s %(message)s'
  )

  # 创建控制台处理器
  console_handler = logging.StreamHandler(sys.stderr)
  console_handler.setFormatter(formatter)

  # 创建文件处理器
  ...

  # 将处理器添加到日志器
  logger.addHandler(console_handler)

  return logger
